# Iris Classifier MLOps Project

> Read in [English](README.md).

Um exemplo de MLOps ponta a ponta para um classificador Iris: [DVC](https://dvc.org/) para versionamento de dados, [MLflow](https://mlflow.org/) para rastreamento de experimentos, e [BentoML](https://www.bentoml.com/) para servir o modelo, em cima do scikit-learn.

Um artigo detalhado sobre a produtização deste projeto — incluindo um remote do DVC que nunca funcionou de verdade — está disponível em [ARTIGO.md](ARTIGO.md) (pt-br) / [ARTIGO.en-us.md](ARTIGO.en-us.md) (en-us).

## Estrutura do projeto

```text
src/
├── config/config.py            # Config (caminho dos dados, nome do modelo, nome do experimento)
├── data/data_loader.py          # lê o CSV local já materializado por `dvc pull`
├── training/train_model.py       # RandomForestClassifier + split treino/teste + acurácia
├── registry/model_registry.py    # loga no MLflow, salva no model store do BentoML
├── serving/iris_service.py        # IrisClassifier (puro, testável) + IrisClassifierService (wrapper @bentoml.service)
└── main.py                        # carrega -> treina -> loga (MLflow) -> salva (BentoML)
```

## Como rodar

```bash
make install    # cria o .venv e instala as deps
make data       # dvc pull - materializa data/iris.csv a partir do remote local do DVC
make train      # treina o modelo, loga no MLflow, salva no model store do BentoML
make serve      # bentoml serve --reload
```

- Swagger UI: http://localhost:3000/docs
- Endpoint da API: `POST http://localhost:3000/classify`
- UI do MLflow: `.venv/bin/mlflow ui` (lê `./mlruns`, gitignorado, gerado localmente por `make train`)

Rodando com Docker (a imagem treina o modelo durante o build, a partir do CSV já puxado pelo CI/por você):

```bash
make docker-build
make docker-run
```

## Desenvolvimento

```bash
make test        # pytest
make coverage     # pytest com relatório de cobertura
make lint         # ruff check
make format       # ruff format
make typecheck    # mypy
```

CI e deploy rodam no Jenkins da plataforma (`Jenkinsfile` → `appPipeline` da Shared Library `platform`, repo devops-platform), disparados por webhooks. Sem GitHub Actions.

- **PRs e branches** — validação do contrato; `docker build --target test` (`ruff check`, `ruff format --check`, `mypy`, `pytest` com cobertura ≥90% em Python 3.11 e 3.12, versões das ferramentas no `config/requirements-dev.txt`); `pip-audit` no `config/requirements.lock`; Trivy (CRITICAL/HIGH) na imagem de runtime.
- **main** — tudo acima e depois build, smoke test, push para o OCIR, deploy atrás do Traefik em https://mlops-iris.137-131-175-7.sslip.io com rollback automático, release com o python-semantic-release (versão, CHANGELOG, tag e release no GitHub) e rebuild do portfolio. Também é reconstruída toda segunda para pegar patches de segurança.
- **Dependências** — Renovate (job `platform/renovate` no Jenkins, `renovate.json` → preset do devops-platform): atualizações diárias, manutenção semanal do lockfile, issue "Dependency Dashboard" e auto-merge de patch/minor depois que o Jenkins aprova.

## Versionamento de dados com DVC

`data/iris.csv` é rastreado pelo DVC (`data/iris.csv.dvc`), com um **remote local versionado no próprio git** (`.dvc-storage/`) em vez de um bucket na nuvem — isso mantém o exemplo totalmente autocontido: `dvc pull` funciona logo após o `git clone`, sem nenhuma credencial de nuvem pra configurar. Troque o remote (`dvc remote modify storage url s3://...`) para um deploy de verdade.
