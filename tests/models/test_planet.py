import json

from sw_planets_api.models.planet import Planet, Film
from sqlalchemy.orm import Session
from datetime import datetime


def test_insert_planet(session: Session):
    p1 = Planet(id=1,
                name="Planet 1",
                climate="Climate 1",
                terrain="Terrain 1")

    session.add(p1)
    session.commit()

    p1_from_db = session.get(Planet, 1)

    assert p1_from_db is not None


def test_insert_planet_with_film_relationship(session: Session):
    p1 = Planet(id=1,
                name="Planet 1",
                climate="Climate 1",
                terrain="Terrain 1")

    f1 = Film(id=1,
              title="Film 1",
              director="Director 1",
              release_date=datetime.now())

    session.add(p1)
    session.add(f1)
    p1.films.append(f1)
    session.commit()

    p1_from_db = session.get(Planet, 1)
    f1_from_db = session.get(Film, 1)

    assert len(p1_from_db.films) == 1
    assert len(f1_from_db.planets) == 1
    assert p1_from_db.films[0].title == "Film 1"
    assert f1_from_db.planets[0].name == "Planet 1"


def test_planet_and_film_serialize():
    f1 = Film(
        id=1,
        title="Film 1",
        director="Director 1",
        release_date=datetime(2022, 2, 12)
    )
    f2 = Film(
        id=2,
        title="Film 2",
        director="Director 2",
        release_date=datetime(2022, 2, 12)
    )
    p = Planet(
        id=1,
        name="Planet_1",
        climate="Climate_1",
        terrain="Terrain_1",
        films=[f1, f2]
    )

    obj = p.serialize()

    assert obj.get("id") == 1
    assert obj.get("name") == "Planet_1"
    assert obj.get("climate") == "Climate_1"
    assert obj.get("terrain") == "Terrain_1"
    assert obj["films"][0].get("id") == 1
    assert obj["films"][0].get("title") == "Film 1"
    assert obj["films"][0].get("director") == "Director 1"
    assert obj["films"][0].get("release_date") == "2022-02-12"
    assert obj["films"][1].get("id") == 2
    assert obj["films"][1].get("title") == "Film 2"
    assert obj["films"][1].get("director") == "Director 2"
    assert obj["films"][1].get("release_date") == "2022-02-12"


def test_planet_from_json_new_planet(session):
    json = {
        "name": "Planet 1",
        "climate": "Climate 1",
        "terrain": "Terrain 1"
    }
    planet = Planet.from_json(session, json, 1)

    assert planet.id == 1
    assert planet.name == "Planet 1"
    assert planet.climate == "Climate 1"
    assert planet.terrain == "Terrain 1"


def test_planet_from_json_existing_planet(session):
    session.add(Planet(id=1, name="Existing Planet", climate="A", terrain="B"))
    session.commit()

    planet = Planet.from_json(session, {}, 1)

    assert planet.id == 1
    assert planet.name == "Existing Planet"
    assert planet.climate == "A"
    assert planet.terrain == "B"


def test_film_from_json_new_film(session):
    json = {
        "title": "Title 1",
        "director": "Director 1",
        "release_date": "2022-10-20"
    }
    film = Film.from_json(session, json, 1)

    assert film.id == 1
    assert film.title == "Title 1"
    assert film.director == "Director 1"
    assert film.release_date == datetime(2022, 10, 20)


def test_film_from_json_existing_film(session):
    session.add(Film(id=1, title="Existing Film", director="A", release_date=datetime(2022, 10, 20)))  # nopep8
    session.commit()

    film = Film.from_json(session, {}, 1)

    assert film.id == 1
    assert film.title == "Existing Film"
    assert film.director == "A"
    assert film.release_date == datetime(2022, 10, 20)
