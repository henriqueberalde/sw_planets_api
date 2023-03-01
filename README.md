# Star Wars Planets Api

Serves Star Wars Planets

## Prerequisites

- Python 3.10
- Poetry 1.2.2
- Docker 23.0.1
- Docker Compose 1.29.2

## Installation
Local
```
poetry install
poetry shell

cd sw_planets_api/db
docker build -t sw_planets_api_db ./
```

Conteinerized
```
docker-compose build
```

## Usage
Local
```
docker run --env MYSQL_DATABASE=db --env MYSQL_ROOT_PASSWORD=root -p 3308:3306 -d -t sw_planets_api_db

python3 sw_planets_api/main.py
```

Conteinerized
```
docker-compose up
```

## API Endpoints

#### Load Planet
```
http://localhost:5000/planets/load/:id

Resquest
curl --location --request POST 'http://localhost:5000/planets/load/123'

Response
{
  "data": {
    "id": 123,
    "name": "Planet 1",
    "climate": "Climate 1",
    "terrain": "Terrain 1",
    "films": [
        {
            "id": 1,
            "title": "Title 1",
            "director": "Director 1",
            "release_date": "2023-01-01",
        }
    ],
  },
  "error": null,
  "success": true
}
```

#### Read a Planet
```
http://localhost:5000/planets/:id

Resquest
curl --location --request GET 'http://localhost:5000/planets/<number>'

Response
{
  "data": {},
  "error": null,
  "success": true
}
```

#### List Planets
```
http://localhost:5000/planets?name=

Resquest
curl --location --request GET 'http://localhost:5000/planets?name=<string>'planet_name/<number>'

Response
{
  "data": [{
    "id": 123,
    "name": "Planet 1",
    "climate": "Climate 1",
    "terrain": "Terrain 1",
    "films": [
        {
            "id": 1,
            "title": "Title 1",
            "director": "Director 1",
            "release_date": "2023-01-01",
        }
    ],
  }],
  "error": null,
  "success": true
}
```

#### Remove Planet
```
http://localhost:5000/planets/:id

Resquest
curl --location --request DELETE 'http://localhost:5000/planets/<number>'

Response
{
  "data": {},
  "error": "cupidatat eu in Lorem",
  "success": true
}
```

## Interative Documentation

[(Swagger) http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)



## Tests

> Installation (to be run only once)
```
cd sw_planets_api/db
docker build -t sw_planets_api_db_test ./
```
> Usage
```
docker run --env MYSQL_DATABASE=db --env MYSQL_ROOT_PASSWORD=root -p 3309:3306 -d -t sw_planets_api_db_test

pytest -v

=================================================== test session starts ===================================================
platform linux -- Python 3.10.8, pytest-7.2.1, pluggy-1.0.0 -- /home/carlosberalde/.cache/pypoetry/virtualenvs/sw-planets-api-bFuQKPsV-py3.10/bin/python
cachedir: .pytest_cache
rootdir: /home/carlosberalde/Projects/sw_planets_api
plugins: cov-4.0.0, mock-3.10.0
collected 16 items                                                                                                        

tests/test_app.py::test_app_get_planets_no_query_string PASSED                                                      [  6%]
tests/test_app.py::test_app_get_planets_id_query_string PASSED                                                      [ 12%]
tests/test_app.py::test_app_get_planets_name_query_string PASSED                                                    [ 18%]
tests/test_app.py::test_app_get_planets_by_id PASSED                                                                [ 25%]
tests/test_app.py::test_app_remove_planet PASSED                                                                    [ 31%]
tests/test_app.py::test_app_remove_planet_with_films PASSED                                                         [ 37%]
tests/models/test_planet.py::test_insert_planet PASSED                                                              [ 43%]
tests/models/test_planet.py::test_insert_planet_with_film_relationship PASSED                                       [ 50%]
tests/models/test_planet.py::test_planet_and_film_serialize PASSED                                                  [ 56%]
tests/models/test_planet.py::test_planet_from_json_new_planet PASSED                                                [ 62%]
tests/models/test_planet.py::test_planet_from_json_existing_planet PASSED                                           [ 68%]
tests/models/test_planet.py::test_film_from_json_new_film PASSED                                                    [ 75%]
tests/models/test_planet.py::test_film_from_json_existing_film PASSED                                               [ 81%]
tests/services/test_star_wars_api_service.py::test_swapi_service_load_planet PASSED                                 [ 87%]
tests/services/test_star_wars_api_service.py::test_swapi_service_load_planet_not_found PASSED                       [ 93%]
tests/services/test_star_wars_api_service.py::test_swapi_service_load_film PASSED                                   [100%]

=================================================== 16 passed in 1.06s ====================================================
```

## Test Coverage
```
pytest --cov=sw_planets_api tests/

=================================================== test session starts ===================================================
platform linux -- Python 3.10.8, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/carlosberalde/Projects/sw_planets_api
plugins: cov-4.0.0, mock-3.10.0
collected 16 items                                                                                                        

tests/test_app.py ......                                                                                            [ 37%]
tests/models/test_planet.py .......                                                                                 [ 81%]
tests/services/test_star_wars_api_service.py ...                                                                    [100%]

---------- coverage: platform linux, python 3.10.8-final-0 -----------
Name                                               Stmts   Miss  Cover
----------------------------------------------------------------------
sw_planets_api/app.py                                 55     15    73%
sw_planets_api/main.py                                11     11     0%
sw_planets_api/models/db.py                           15      2    87%
sw_planets_api/models/planet.py                       48      1    98%
sw_planets_api/services/star_wars_api_service.py      28      2    93%
----------------------------------------------------------------------
TOTAL                                                157     31    80%


=================================================== 16 passed in 0.97s ====================================================
```

## Logging

Log information is written, by default, into the file `sw_planets_api.log`


## Improvements

> Every project is a working in progress project for me

Possible improvements:

- [ ] Add migration lib (ex: alembic)
- [ ] Add makefile
- [ ] 


## TODO

> This section was built when the project was started, I didn`t remove it to show my mind organization during the test

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
- [x] Log
- [x] Api Documentation (with examples)
- [ ] Test conteinerized env
- [x] Remove print
