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


def test_planet_film_relationship(session: Session):
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
