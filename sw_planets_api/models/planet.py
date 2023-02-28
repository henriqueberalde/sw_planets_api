import sw_planets_api.models.db as db

from sqlalchemy import Column, Integer, String


class Planet(db.Base):
    __tablename__ = "planets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    climate = Column(String)
    terrain = Column(String)

    def test(self):
        return "TEST"
