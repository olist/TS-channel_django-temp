# [TECH-START] TS: sistema gerenciamento de channels.

## Descrição

Desafio: sistema gerenciamento de channels.

Construído sobre uma plataforma Python 3, Poetry, Pytest, Flake8, Docker, Docker-Compose, Postgresql.

## Instruções instalação e execução com docker-compose:

- Configure as opções de: migrations, user_admin, pytest (com ou sem relatório) e runserver, em:

> *[run.sh](https://github.com/olist/TS-channel_django-temp/blob/main/run.sh)*

- No terminal execute:

```sh
docker-compose up --build
```

## Instruções de instalação local:

- Instale o Python:

```sh
pyenv local 3.9.5
```

- Configure o ambiente virtual:

```sh
poetry install
```

- Acesse o ambiente virtual:

```sh
poetry shell
```

## Autor(es):

- Danilo, Fernanda, Matheus e Victor.