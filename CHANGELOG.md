# CHANGELOG

<!-- version list -->

## v1.0.6 (2026-11-15)

### Bug Fixes

- **docker**: Use python 3.14 so the wheels install, and upgrade pip so the scan passes
  ([#40](https://github.com/thentsation/mlops-iris-classifier/pull/40),
  [`5cabc09`](https://github.com/thentsation/mlops-iris-classifier/commit/5cabc098ef3bf05c3552d5a5af4d604d2e77d64c))

### Chores

- **ci**: Bump astral-sh/setup-uv from 10.3.2 to 10.3.3
  ([#31](https://github.com/thentsation/mlops-iris-classifier/pull/31),
  [`890926f`](https://github.com/thentsation/mlops-iris-classifier/commit/890926f66e24dfff18b0b204350bb1b9961c4028))

- **ci**: Bump peter-evans/create-pull-request from 8.1.1 to 8.1.2
  ([#35](https://github.com/thentsation/mlops-iris-classifier/pull/35),
  [`c982d62`](https://github.com/thentsation/mlops-iris-classifier/commit/c982d626a749b68ee45c484fe26d8e80262c1eb1))

- **ci**: Bump peter-evans/create-pull-request from 8.1.2 to 8.1.3
  ([#39](https://github.com/thentsation/mlops-iris-classifier/pull/39),
  [`79dbc6b`](https://github.com/thentsation/mlops-iris-classifier/commit/79dbc6b8ef9708683875b14d53258d9c21c9df8a))

- **deps**: Bump mypy from 2.4.0 to 2.4.1 in /config
  ([#33](https://github.com/thentsation/mlops-iris-classifier/pull/33),
  [`47eaf00`](https://github.com/thentsation/mlops-iris-classifier/commit/47eaf00a4083c28b8337ae46a75d0c980a01ea7d))

- **deps**: Bump pytest from 9.1.1 to 9.2.0 in /config
  ([#32](https://github.com/thentsation/mlops-iris-classifier/pull/32),
  [`bd0a09f`](https://github.com/thentsation/mlops-iris-classifier/commit/bd0a09f9c40ef254a81c3a748ac0804f38fde7ce))

- **deps**: Bump python from 3.12-slim to 3.15-slim in /docker
  ([#34](https://github.com/thentsation/mlops-iris-classifier/pull/34),
  [`14d8b6c`](https://github.com/thentsation/mlops-iris-classifier/commit/14d8b6c485fd59259a7cb84a4c8e894a203fce38))

- **deps**: Bump ruff from 0.17.2 to 0.17.3 in /config
  ([#30](https://github.com/thentsation/mlops-iris-classifier/pull/30),
  [`1310353`](https://github.com/thentsation/mlops-iris-classifier/commit/13103530007f85be0c1bb022d6e973af7fc11353))

- **deps**: Bump ruff from 0.17.3 to 0.17.4 in /config
  ([#38](https://github.com/thentsation/mlops-iris-classifier/pull/38),
  [`0e87467`](https://github.com/thentsation/mlops-iris-classifier/commit/0e874677f463ef961c30c2c6c1cc68f26f4ec4ef))

- **deps**: Update bentoml requirement in /config
  ([#29](https://github.com/thentsation/mlops-iris-classifier/pull/29),
  [`2bec9d4`](https://github.com/thentsation/mlops-iris-classifier/commit/2bec9d422fe34bbb188665faffe968614da662ec))

- **deps**: Update lockfile ([#28](https://github.com/thentsation/mlops-iris-classifier/pull/28),
  [`c57acb1`](https://github.com/thentsation/mlops-iris-classifier/commit/c57acb185b63b3334663bd241ae536af2826de5c))

- **deps**: Update mlflow requirement in /config
  ([#37](https://github.com/thentsation/mlops-iris-classifier/pull/37),
  [`d80471b`](https://github.com/thentsation/mlops-iris-classifier/commit/d80471be704d6dd660089dda6ef40890bd7cfa3a))

- **deps**: Update pandas requirement in /config
  ([#36](https://github.com/thentsation/mlops-iris-classifier/pull/36),
  [`5697a49`](https://github.com/thentsation/mlops-iris-classifier/commit/5697a498d8a7ca24cf192a1d7da67b079311d3f7))


## v1.0.5 (2026-10-26)

### Bug Fixes

- **deps**: Upgrade lockfile and use --upgrade in lockfile workflow
  ([#27](https://github.com/thentsation/mlops-iris-classifier/pull/27),
  [`673137b`](https://github.com/thentsation/mlops-iris-classifier/commit/673137b3a8c19a7965bc128fac8d409caa0ba3f4))

- **deps**: Use --upgrade when regenerating the lockfile
  ([#27](https://github.com/thentsation/mlops-iris-classifier/pull/27),
  [`673137b`](https://github.com/thentsation/mlops-iris-classifier/commit/673137b3a8c19a7965bc128fac8d409caa0ba3f4))

### Chores

- **ci**: Bump astral-sh/setup-uv from 10.2.0 to 10.3.0
  ([#18](https://github.com/thentsation/mlops-iris-classifier/pull/18),
  [`46ab83a`](https://github.com/thentsation/mlops-iris-classifier/commit/46ab83a63c5d043387fbf335d1ec1459a68dfca8))

- **ci**: Bump astral-sh/setup-uv from 10.3.0 to 10.3.2
  ([#26](https://github.com/thentsation/mlops-iris-classifier/pull/26),
  [`ce3aa3e`](https://github.com/thentsation/mlops-iris-classifier/commit/ce3aa3ea6e685ce45f7b5e5689842ae35677adc5))

- **deps**: Bump ruff from 0.16.10 to 0.17.0 in /config
  ([#19](https://github.com/thentsation/mlops-iris-classifier/pull/19),
  [`4ca24e7`](https://github.com/thentsation/mlops-iris-classifier/commit/4ca24e74cd802384e64d313d4b24f4d2b871b0b4))

- **deps**: Bump ruff from 0.17.0 to 0.17.1 in /config
  ([#22](https://github.com/thentsation/mlops-iris-classifier/pull/22),
  [`4178f79`](https://github.com/thentsation/mlops-iris-classifier/commit/4178f792759f50474c4425275567efcf1f515866))

- **deps**: Bump ruff from 0.17.1 to 0.17.2 in /config
  ([#25](https://github.com/thentsation/mlops-iris-classifier/pull/25),
  [`08e886a`](https://github.com/thentsation/mlops-iris-classifier/commit/08e886ac5a31a228198cf290532f2ecbae2d66bb))

- **deps**: Refresh pip-compile outputs
  ([#9](https://github.com/thentsation/mlops-iris-classifier/pull/9),
  [`8f82b6b`](https://github.com/thentsation/mlops-iris-classifier/commit/8f82b6b1ac46d16b9c50a721cc65845716da9db6))

- **deps**: Update bentoml requirement in /config
  ([#15](https://github.com/thentsation/mlops-iris-classifier/pull/15),
  [`194cf63`](https://github.com/thentsation/mlops-iris-classifier/commit/194cf630455b215d070fd59a57fef112db3fb666))

- **deps**: Update dependency mlflow to >=3.17,<3.18
  ([#10](https://github.com/thentsation/mlops-iris-classifier/pull/10),
  [`46a923e`](https://github.com/thentsation/mlops-iris-classifier/commit/46a923e2a9397bbb94449644875e8c8cd8cd52e7))

- **deps**: Update dependency mypy to v2.4.0
  ([#6](https://github.com/thentsation/mlops-iris-classifier/pull/6),
  [`f48f8d3`](https://github.com/thentsation/mlops-iris-classifier/commit/f48f8d3459cd0e7e08a679342732b77b9f8a243e))

- **deps**: Update dependency opentelemetry-proto to <1.46
  ([#7](https://github.com/thentsation/mlops-iris-classifier/pull/7),
  [`4221f6e`](https://github.com/thentsation/mlops-iris-classifier/commit/4221f6eab5ccf481bb02b2e758479fb3d79caa7d))

- **deps**: Update dependency ruff to v0.16.10
  ([#5](https://github.com/thentsation/mlops-iris-classifier/pull/5),
  [`50ade2b`](https://github.com/thentsation/mlops-iris-classifier/commit/50ade2b61631d3117926e3fe7c6ef06fb710d366))

- **deps**: Update dvc requirement in /config
  ([#13](https://github.com/thentsation/mlops-iris-classifier/pull/13),
  [`85f8330`](https://github.com/thentsation/mlops-iris-classifier/commit/85f8330358cbc07b9fe02c086b3e9ad85debd788))

- **deps**: Update lockfile ([#27](https://github.com/thentsation/mlops-iris-classifier/pull/27),
  [`673137b`](https://github.com/thentsation/mlops-iris-classifier/commit/673137b3a8c19a7965bc128fac8d409caa0ba3f4))

- **deps**: Update mlflow requirement in /config
  ([#23](https://github.com/thentsation/mlops-iris-classifier/pull/23),
  [`6beb69a`](https://github.com/thentsation/mlops-iris-classifier/commit/6beb69a652e223660e2420122ce948849bdade3a))

- **deps**: Update mlflow requirement in /config
  ([#21](https://github.com/thentsation/mlops-iris-classifier/pull/21),
  [`2036426`](https://github.com/thentsation/mlops-iris-classifier/commit/20364268744e501e6ed4ecb8d8ab076dfbe07d06))

- **deps**: Update pandas requirement in /config
  ([#24](https://github.com/thentsation/mlops-iris-classifier/pull/24),
  [`1139378`](https://github.com/thentsation/mlops-iris-classifier/commit/11393780d08d1190ef7e95ecdb2ce75c16d14340))

- **deps**: Update pandas requirement in /config
  ([#12](https://github.com/thentsation/mlops-iris-classifier/pull/12),
  [`c55711b`](https://github.com/thentsation/mlops-iris-classifier/commit/c55711b4030045134f53146d71da562240289187))

- **deps**: Update scikit-learn requirement in /config
  ([#14](https://github.com/thentsation/mlops-iris-classifier/pull/14),
  [`3f4e118`](https://github.com/thentsation/mlops-iris-classifier/commit/3f4e11843fe9dc561819568c38d946eb0fe8681a))

### Continuous Integration

- Pipeline da Shared Library da plataforma e Renovate
  ([#4](https://github.com/thentsation/mlops-iris-classifier/pull/4),
  [`565b51d`](https://github.com/thentsation/mlops-iris-classifier/commit/565b51d3cee79c5c0ddf849b7442ddf5126e3903))

- Remove workflow notify-portfolio (token sem acesso; o portfolio atualiza pelo cron diário)
  ([#16](https://github.com/thentsation/mlops-iris-classifier/pull/16),
  [`1d0e313`](https://github.com/thentsation/mlops-iris-classifier/commit/1d0e3133391c41f4b885b3bb25f9028211a79643))


## v1.0.4 (2026-09-28)

### Bug Fixes

- **ci**: Open lockfile PRs with RELEASE_PAT so CI runs on them
  ([`89f353c`](https://github.com/thentsation/mlops-iris-classifier/commit/89f353c75564ebb5241e16e1a270f841878613b1))


## v1.0.3 (2026-09-28)

### Bug Fixes

- Use RELEASE_PAT so dependabot auto-merge can write to PRs
  ([`83a9a56`](https://github.com/thentsation/mlops-iris-classifier/commit/83a9a56f3cbe17727256728f3edf8143e6106793))


## v1.0.2 (2026-09-26)

### Bug Fixes

- Broaden Trivy's pip/_vendor skip-dirs to a recursive glob
  ([`297b485`](https://github.com/thentsation/mlops-iris-classifier/commit/297b4854ec93129ed3a33652d22dab0ae93fcf9f))


## v1.0.1 (2026-09-26)

### Bug Fixes

- Pull DVC data in the push-ghcr job too
  ([`98fd8c4`](https://github.com/thentsation/mlops-iris-classifier/commit/98fd8c4dac89b8ec22e60fc81ea00935c3b410c7))

### Chores

- Remove the stale root requirements.txt
  ([`8096565`](https://github.com/thentsation/mlops-iris-classifier/commit/80965653b7d5bfc4ce239162ee9469f693ef67d5))
