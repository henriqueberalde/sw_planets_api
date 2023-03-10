import sw_planets_api.models.db as db

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime


def dump_datetime(value: Column[DateTime]):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None

    return value.strftime("%Y-%m-%d")


class Planet(db.Base):
    __tablename__ = "planets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    terrain = Column(String)
    films = relationship(
        "Film",
        secondary="planets_films",
        back_populates="planets"
    )

    def serialize(self):
        return {
           "id": self.id,
           "name": self.name,
           "climate": self.climate,
           "terrain": self.terrain,
           "films": [f.serialize() for f in self.films]
        }

    @staticmethod
    def from_json(session, json, id) -> "Planet":
        from_db: Planet = session.get(Planet, id)

        if from_db is not None:
            return from_db

        name = json.get("name")
        climate = json.get("climate")
        terrain = json.get("terrain")

        return Planet(
            id=id,
            name=name,
            climate=climate,
            terrain=terrain
        )


class Film(db.Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_date = Column(DateTime)
    planets = relationship(
        "Planet",
        secondary="planets_films",
        back_populates="films"
    )

    def serialize(self):
        return {
           "id": self.id,
           "title": self.title,
           "director": self.director,
           "release_date": dump_datetime(self.release_date)
        }

    @staticmethod
    def from_json(session, json, id) -> "Film":
        from_db: Film = session.get(Film, id)
        if from_db is not None:
            return from_db

        title = json.get("title")
        director = json.get("director")
        release_date = datetime.strptime(json.get("release_date"), "%Y-%m-%d")

        return Film(
            id=id,
            title=title,
            director=director,
            release_date=release_date
        )


class PlanetsFilms(db.Base):
    __tablename__ = "planets_films"

    id_planet = Column(Integer,
                       ForeignKey("planets.id"),
                       primary_key=True)
    id_film = Column(Integer,
                     ForeignKey("films.id"),
                     primary_key=True)
