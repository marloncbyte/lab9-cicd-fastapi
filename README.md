# LAB9 - Pipeline CI/CD com FastAPI, Docker e AWS EC2

Projeto-base para demonstrar deploy automatico em homologacao (`develop`) e deploy em producao (`main`) protegido por aprovacao do GitHub Environment.

## Estrutura

- `app/main.py`: API FastAPI com `/` e `/health`.
- `tests/`: testes automatizados.
- `Dockerfile`: imagem da aplicacao.
- `.github/workflows/python-app.yml`: build, testes, publicacao no Docker Hub e deploy por SSH.
- `scripts/ec2-install-docker.sh`: instalacao do Docker em Amazon Linux 2023.

## Fluxo

- Pull request para `develop` ou `main`: executa lint e testes.
- Push em `develop`: build/testes, publica imagem e faz deploy automatico na EC2 de homologacao na porta 8080.
- Push em `main`: build/testes, publica imagem e aguarda aprovacao no Environment `producao` antes do deploy na EC2 de producao.

## Configuracao no GitHub

Em **Settings > Secrets and variables > Actions**, configure:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `HML_EC2_HOST`, `HML_EC2_USERNAME`, `HML_EC2_SSH_KEY`
- `EC2_HOST`, `EC2_USERNAME`, `EC2_SSH_KEY` (producao)

Em **Settings > Environments**, crie `homologacao` e `producao`. No ambiente `producao`, habilite **Required reviewers**. O deploy depende de duas EC2 previamente preparadas com Docker, SSH e porta TCP 8080 liberada conforme a necessidade.

## Teste local

```bash
pip install -r requirements-dev.txt
flake8 app tests
pytest -v
uvicorn app.main:app --reload
```

Acesse `http://127.0.0.1:8000/health`.

## Observacao

A infraestrutura AWS nao e criada automaticamente por este repositorio. As instancias EC2 e seus Security Groups precisam ser configurados no AWS Academy/Vocareum. Homologacao usa secrets com prefixo `HML_`; `EC2_HOST`, `EC2_USERNAME` e `EC2_SSH_KEY` sao reservados para producao. A imagem e versionada pelo SHA do commit para que cada deploy use a versao correspondente ao codigo testado.
