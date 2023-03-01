import pytest
import sw_planets_api.models.db as db

from sw_planets_api.app import create_app
from sqlalchemy.orm import Session


__session = Session(db.get_engine("mysql+pymysql://root:root@localhost:3309/db"))  # nopep8


@pytest.fixture()
def session(scope="function") -> Session:
    __session.expunge_all()
    __session.execute("DELETE FROM planets_films;")
    __session.execute("DELETE FROM planets;")
    __session.execute("DELETE FROM films;")

    __session.execute("ALTER TABLE planets_films AUTO_INCREMENT = 1;")
    __session.execute("ALTER TABLE planets AUTO_INCREMENT = 1;")
    __session.execute("ALTER TABLE films AUTO_INCREMENT = 1;")
    __session.commit()

    return __session


@pytest.fixture()
def app(session):
    return create_app(session)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
