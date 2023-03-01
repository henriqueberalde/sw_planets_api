import json as json

from sw_planets_api.models.planet import Planet, Film, PlanetsFilms
from flask.testing import FlaskClient


def test_app_get_planets_no_query_string(client):
    res = client.get("/planets")

    assert res.status_code == 200
    assert res.data == b'{"data":[],"error":null,"success":true}\n'


def test_app_get_planets_id_query_string(session, client: FlaskClient):
    p1 = Planet(id=1, name="Planet_1")
    p2 = Planet(id=2, name="Planet_2")
    session.add(p1)
    session.add(p2)
    session.commit()

    res = client.get("/planets?id=1")

    body_obj = json.loads(res.get_data(as_text=True))

    assert res.status_code == 200
    assert body_obj.get("data")[0].get("name") == "Planet_1"
    assert len(body_obj.get("data")) == 1
    assert body_obj.get("error") is None
    assert body_obj.get("success") is True


def test_app_get_planets_name_query_string(session, client: FlaskClient):
    p1 = Planet(id=1, name="Planet_1")
    p2 = Planet(id=2, name="Planet_2")
    session.add(p1)
    session.add(p2)
    session.commit()

    res = client.get("/planets?name=Planet_2")

    body_obj = json.loads(res.get_data(as_text=True))

    assert res.status_code == 200
    assert body_obj.get("data")[0].get("name") == "Planet_2"
    assert len(body_obj.get("data")) == 1
    assert body_obj.get("error") is None
    assert body_obj.get("success") is True


def test_app_get_planets_by_id(session, client: FlaskClient):
    p1 = Planet(id=1, name="Planet_1")
    p2 = Planet(id=2, name="Planet_2")
    session.add(p1)
    session.add(p2)
    session.commit()

    res = client.get("/planets/2")

    body_obj = json.loads(res.get_data(as_text=True))

    assert res.status_code == 200
    assert body_obj.get("data").get("name") == "Planet_2"
    assert body_obj.get("error") is None
    assert body_obj.get("success") is True


def test_app_remove_planet(session, client: FlaskClient):
    p1 = Planet(id=1, name="Planet_1")
    session.add(p1)
    session.commit()

    res = client.delete("/planets/1")

    body_obj = json.loads(res.get_data(as_text=True))

    assert res.status_code == 200
    assert body_obj.get("data") is None
    assert body_obj.get("error") is None
    assert body_obj.get("success") is True
    assert session.get(Planet, 1) is None


def test_app_remove_planet_with_films(session, client: FlaskClient):
    p1 = Planet(id=1, name="Planet_1")
    f1 = Film(id=1, title="Film_1")
    p1.films.append(f1)
    session.add(p1)
    session.commit()

    res = client.delete("/planets/1")

    body_obj = json.loads(res.get_data(as_text=True))

    assert res.status_code == 200
    assert body_obj.get("data") is None
    assert body_obj.get("error") is None
    assert body_obj.get("success") is True
    assert session.get(Planet, 1) is None
    assert len(session.query(PlanetsFilms, 1).all()) == 0
