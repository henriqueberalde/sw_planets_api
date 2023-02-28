import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

env = os.getenv("SW_PLANET_API_ENV")
conn_string = "mysql+pymysql://root:root@localhost:3308/db"

if env == "container":
    conn_string = "mysql+pymysql://root:root@sw_planets_db/db"


def get_engine(conn_string: str = conn_string) -> Engine:  # nopep8
    return create_engine(conn_string)


def get_session() -> Session:
    return Session(get_engine())


Base = declarative_base(get_engine())
