import pytest
import sw_planets_api.models.db as db
from sqlalchemy.orm import Session


__session = Session(db.get_engine("mysql+pymysql://root:root@localhost:3309/db"))  # nopep8


@pytest.fixture()
def session(scope="function") -> Session:
    __session.expunge_all()
    __session.execute("DELETE FROM planets;")

    __session.execute("ALTER TABLE planets AUTO_INCREMENT = 1;")
    __session.commit()

    return __session
