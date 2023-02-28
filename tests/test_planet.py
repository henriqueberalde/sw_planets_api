from sw_planets_api.models.planet import Planet
from sqlalchemy.orm import Session


def test_method_test():
    expected = "TEST"

    p = Planet()
    result = p.test()

    assert result == expected


def test_db(session: Session):
    planet_name = "Planet1"
    p1 = Planet(name=planet_name)

    session.add(p1)
    session.commit()

    p1_from_db = session.query(Planet).filter_by(name=planet_name).one()

    assert p1_from_db is not None
