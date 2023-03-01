# Star Wars Planets Api

Serves Star Wars Planets data

## Prerequisites

- Python 3.10
- Poetry 1.2.2
- Docker 23.0.1
- Docker Compose 1.29.2

## Installation
Conteinerized
```
docker-compose build
```

Local
```
poetry install
poetry shell

cd sw_planets_api/db
docker build -t sw_planets_api_db ./
```

Test
```
cd sw_planets_api/db
docker build -t sw_planets_api_db_test ./
```

## Usage
??? Documentation ??? 

Conteinerized
```
docker-compose up
```

Local
```
docker run --env MYSQL_DATABASE=db --env MYSQL_ROOT_PASSWORD=root -p 3308:3306 -d -t sw_planets_api_db

python3 sw_planets_api/main.py
```

## Tests
```
docker run --env MYSQL_DATABASE=db --env MYSQL_ROOT_PASSWORD=root -p 3309:3306 -d -t sw_planets_api_db_test

pytest -v
```

Coverage
```
pytest --cov=sw_planets_api tests/
```

## Logging

Log information is written, by default, into the file '???.log'


## Improvements

> Every project is a working in progress project for me

Possible improvements:

- [ ] Add migration lib (ex: alembic)
- [ ] 


## TODO

> This section was built when the project was started, I didn`t remove it to show my mind organization

- [x] Init git
- [x] Init poetry (pyproject.toml)
- [x] Gitignore
- [x] README.md
- [x] Setup Linter
- [x] Setup pytest
- [x] Setup Logging
- [x] Setup Docker
- [x] Setup DB
- [x] Setup ORM
- [x] Setup DB and ORM for test
- [x] Create Entities Planet and Film
- [x] Setup api lib (Flask)
- [x] `Endpoint` Load planet from api by id
- [x] `Endpoint` List all planets
- [x] `Endpoint` Search planet by name
- [x] `Endpoint` Search planet by id
- [x] `Endpoint` Remove Planet
- [x] Global response pattern for all requests
- [x] Test Coverage
- [ ] Log
- [ ] Api Documentation (with examples)

- [ ] Check Content-Type on header
- [ ] Remove all single braquets
- [ ] Test conteinerized env
- [ ] Try to put all type annotations
- [ ] Remove print

        