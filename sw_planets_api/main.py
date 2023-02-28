import sys
import logging

import sw_planets_api.models.db as db
from sw_planets_api.models.planet import Planet


logging.basicConfig(
        filename="sw_planets_api.log",
        format="%(asctime)s:%(levelname)s:%(message)s",
        encoding="utf-8",
        level=logging.DEBUG
    )


def print_all_planets():
    session = db.get_session()
    planets = session.query(Planet).all()

    for planet in planets:
        print(planet.name)


def planet_test():
    p = Planet()
    p.test


def main() -> None:
    print_all_planets()

    planet_test()


if __name__ == "__main__":
    sys.exit(main())
