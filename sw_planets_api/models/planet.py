import sw_planets_api.models.db as db

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Planet(db.Base):
    __tablename__ = "planets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    terrain = Column(String)
    films = relationship(
        'Film',
        secondary='planets_films',
        back_populates='planets'
    )


class Film(db.Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_date = DateTime
    planets = relationship(
        'Planet',
        secondary='planets_films',
        back_populates='films'
    )


class PlanetsFilms(db.Base):
    __tablename__ = "planets_films"

    id_planet = Column(Integer,
                       ForeignKey('planets.id'),
                       primary_key=True)
    id_film = Column(Integer,
                     ForeignKey('films.id'),
                     primary_key=True)
