### Tecnologías:
poetry
python v3.10.12 (Deseable usar versionador recomendable: Pyenv)
django 5.1.1
django rest framework 3.15.2

### Tecnologías a implementar
redis
graphql
postgresql
docker
kubernetes
aws

### Instalacion de poetry

```bash
1.- curl -sSL https://install.python-poetry.org | python3 -
2.- export PATH="$HOME/.local/bin:$PATH"
3.- source ~/.bashrc   # Para Bash
    source ~/.zshrc    # Para Zsh
4.- poetry --version (probar version)
```

### Iniciar un proyecto con poetry

```bash
1.- poetry init (para iniciar un proyecto)
$ package name [poetry]: <name_project_poetry> (dejar vacío (enter))
$ version [0.1.0]: nil
$ description [ '' ] : nil
$ author [...., skip]: nil
$ license [..]: nil
$ compatible python versions [3.9]: nil
$ question1: no
$ question2: no
$ question3: yes
```

## Instalamos las dependencias del proyecto que estan en poetry

```bash
1.- poetry install
```

## Ver la lista
```bash
poetry env list
```

### Django viene por defecto como base de datos "SQLite"
Creando proyecto con Django:

```python
1.- django-admin startproject <name_project>
```

creando una app con Django

```python
2.- python3 manage.py startapp <name_app>
```

Creando un "suerusuario" de Django

```python
3.- python3 manage.py createsuperuser
```

fields:
- email
- password

Iniciamos nuestro proyecto

```python
4.- python3 manage.py runserver
```
### Panel admin de Django
```python
http://127.0.0.1:8000/admin/
```

### APi Swagger
```python
http://127.0.0.1:8000/docs/
```