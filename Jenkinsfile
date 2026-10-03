// Pipeline da plataforma (Shared Library "platform", repo devops-platform/jenkins-lib).
// PRs e branches: validação, CI (docker build --target test), pip-audit e Trivy.
// main: build, smoke test, push, deploy atrás do Traefik com rollback, release
// (semantic-release), rebuild do portfolio e rebuild semanal.
@Library('platform') _

appPipeline(
    name: 'mlops-iris-classifier',
    host: 'mlops-iris.137-131-175-7.sslip.io',
    healthPath: '/healthz',
    // O /healthz do BentoML não devolve a versão.
    healthExpectsVersion: false,
    deployBranch: 'main',
    // PYSEC-2026-2447: o diskcache (transitivo via dvc-data) usa pickle no cache em disco;
    // explorar exige escrita local no diretório do cache, que já é comprometimento total
    // no CI/dev. Sem correção publicada.
    pipAuditIgnore: ['PYSEC-2026-2447'],
    notify: [[repo: 'ntsation/portfolio', event: 'rebuild']],
)
