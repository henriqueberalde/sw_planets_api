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

## Usage
??? Documentation ??? 

Conteinerized
```
docker-compose up
```

Local
Run db on a separated terminal
```
docker run --env MYSQL_DATABASE=db --env MYSQL_ROOT_PASSWORD=root -p 3308:3306 -t sw_planets_api_db
```

```
python3 sw_planets_api/main.py
```

## Tests
```
pytest -v
```

## Logging

Log information is written, by default, into the file '???.log'


## Improvements

> Every project is a working in progress project for me

Possible improvements:

- [ ] Add migration lib (ex alembic)
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
- [ ] Setup DB and ORM for test
- [ ] Create Entities Planet and Film
- [ ] Setup api lib
- [ ] Load planet from api by id
- [ ] List all planets
- [ ] Search planet by name
- [ ] Search planet by id
- [ ] Remove Planet
- [ ] Documentation



https://swapi.dev/about

https://swapi.dev/documentation

https://swapi.dev/

Planets (https://swapi.dev/api/planets)
    name
    climate
    terrain
    films (https://swapi.dev/api/films/1/)
        title
        director
        release_date
        