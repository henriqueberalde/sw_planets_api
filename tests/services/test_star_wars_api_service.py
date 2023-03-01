import pytest
import datetime

from sqlalchemy.orm import Session
from sw_planets_api.models.planet import Film
from sw_planets_api.services.star_wars_api_service import StarWarsApiService
from pytest_mock.plugin import MockerFixture
from requests import Response
from pytest_mock._util import _mock_module


def test_swapi_service_load_planet(session: Session, mocker: MockerFixture):
    mock_response = _mock_module.Mock(json=lambda: {
        "id": 1,
        "name": "Tatooine",
        "climate": "arid",
        "terrain": "desert",
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/4/",
            "https://swapi.dev/api/films/5/",
            "https://swapi.dev/api/films/6/"
        ]
    })

    mocker.patch("requests.get", return_value=mock_response)
    mocker.patch("sw_planets_api.models.planet.Film.from_json", return_value=Film())  # nopep8

    planet = StarWarsApiService.load_planet(session, 1)

    assert planet.id == 1
    assert planet.name == "Tatooine"
    assert planet.climate == "arid"
    assert planet.terrain == "desert"
    assert len(planet.films) == 5


def test_swapi_service_load_planet_not_found(session, mocker):
    mock_response = _mock_module.Mock(json=lambda: {
        "detail": "Not found"
    })

    mocker.patch("requests.get", return_value=mock_response)

    with pytest.raises(
            Exception,
            match="Planet 12345 not found on star wars api. Please check id number again on https://swapi.dev/"):
        StarWarsApiService.load_planet(session, 12345)


def test_swapi_service_load_film(session, mocker):
    mock_response = _mock_module.Mock(json=lambda: {
        "id": 1,
        "title": "Title 1",
        "director": "Director 1",
        "release_date": "2022-10-20"
    })

    mocker.patch("requests.get", return_value=mock_response)

    planet = StarWarsApiService.load_film(session, "https://swapi.dev/api/films/1/")  # nopep8

    assert planet.id == 1
    assert planet.title == "Title 1"
    assert planet.director == "Director 1"
    assert planet.release_date == datetime.datetime(2022, 10, 20)
