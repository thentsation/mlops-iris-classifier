🇧🇷 Português | [🇺🇸 English](ARTIGO.en-us.md)

# O DVC que nunca puxou dado nenhum

Esse projeto se vende como "MLOps de verdade": DVC pra dados, MLflow pra experimentos, BentoML pra servir. Três peças reais. O problema é que uma delas nunca funcionou — o remote do DVC apontava pra `/home/ntsation/docs/mlops-iris-classifier/dvc`, um caminho absoluto na máquina antiga onde o projeto foi criado. `dvc pull` em qualquer outro lugar (inclusive no CI, inclusive num clone novo) falhava silenciosamente ou nem rodava, porque ninguém nunca chegou a testar o fluxo do zero.

## O que eu tinha em mãos

Uma estrutura duplicada — parte do código em `src/` (camadas `data`, `training`, `registry`, `utils`) seguindo SOLID, e parte solta na raiz (`services/iris_services.py`, `train.py`, `config/`) sobrevivendo de uma migração que não terminou. Um `models/models.pkl` de 0 bytes. Bytecode `.pyc` commitado no git (`src/__pycache__/`). Um `bentofile.yaml` apontando pra `src.serve:svc`, um módulo que não existe. E o serviço BentoML na API antiga (`bentoml.io.NumpyNdarray`, `Service(...)`), enquanto os outros projetos da organização já usam o decorator `@bentoml.service`.

## Consertando o DVC de verdade, não só a aparência

Reconfigurei o remote pra um diretório local **versionado no próprio git** (`.dvc-storage/`), regenerei `data/iris.csv` a partir do dataset embutido do scikit-learn (o CSV original nunca foi commitado — só o ponteiro `.dvc`, sem o blob real em lugar nenhum), rodei `dvc add` + `dvc push`, e testei o ciclo completo: apagar `data/iris.csv`, rodar `dvc pull`, confirmar que ele volta. Agora é autocontido — clonou o repo, `dvc pull` funciona, sem nenhuma credencial de nuvem.

```text
$ rm data/iris.csv && dvc pull
A       data/iris.csv
1 file added
```

## Uma decisão que troquei de ideia no meio do caminho

Minha primeira versão do `DataLoader` mantinha `dvc.api.get_url()` — resolver a URL do dado via API do DVC antes de ler com pandas. Fazia sentido na minha cabeça: "é assim que se usa DVC". Só que ao empacotar o treino no Docker, isso quebrou: `dvc.api.get_url()` exige um repositório git funcional, e a imagem final não tem `.git` (só copiei `src/` e o CSV já materializado, de propósito, pra manter a imagem pequena).

Parei pra pensar no fluxo real: o pipeline inteiro já faz `dvc pull` **antes** de treinar (no `make train`, no CI, na etapa que precede o build da imagem) — nesse ponto o arquivo já está no disco, materializado. Chamar `dvc.api.get_url()` de novo dentro do código Python era redundante e, pior, era o que estava quebrando o Docker. `DataLoader` virou um `pd.read_csv()` direto:

```python
class DataLoader:
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)
```

O DVC continua fazendo o trabalho dele — versionar e materializar o dado — só que fora do código de treino, onde ele pertence.

## Modernizando o serviço BentoML e achando um bug de import só depois de rodar de verdade

Reescrevi o serviço no padrão `@bentoml.service` (igual ao `iris-classification-bentoml`), separando `IrisClassifier` (puro, recebe o modelo por injeção, testável sem o runtime do BentoML) do wrapper decorado. `mypy` e os testes passaram de primeira. O que só apareceu quando eu de fato subi o container e bati no endpoint: `bentoml serve src.serving.iris_service:IrisClassifierService` falhava com `No module named 'config'`.

A causa: `bentoml serve <módulo>` importa o serviço pelo caminho pontilhado a partir do diretório de trabalho (`/app` no path, então `src.serving...` resolve) — mas o código dentro do módulo faz `from config.config import Config`, um import "bare" que só resolve se `/app/src` **também** estiver no path. Rodar `python src/main.py` funciona sem configurar nada porque o Python já coloca o diretório do script (`/app/src`) no `sys.path`; `bentoml serve` não faz esse favor. Faltava `ENV PYTHONPATH=/app/src` no Dockerfile — e esse mesmo bug já estava, sem eu perceber, no `iris-classification-bentoml`, publicado há dois dias. Corrigi os dois.

## O resto do padrão

CI completo (ruff, pytest com piso de 90%, mypy, pip-audit, Docker+Trivy+GHCR, dependabot, release semântico), com um ajuste: o job Docker do CI roda `dvc pull` antes do build, já que a imagem espera `data/iris.csv` materializado no contexto. `pip-audit` ficou limpo depois de trocar as versões arqueológicas do `requirements.txt` original (BentoML 1.0.15, MLflow 2.3.1, scikit-learn 1.2.2, pandas 1.5.3 — tudo de 2023) pelas atuais, e de silenciar uma CVE sem correção publicada no `diskcache` (dependência transitiva do `dvc-data`, usa pickle no cache local — exige acesso de escrita ao diretório de cache pra ser explorado, ou seja, quem exploraria isso já teria acesso total à máquina).
