import sys
import logging
import sw_planets_api.models.db as db

from sw_planets_api.models.planet import Planet
from app import create_app

logging.basicConfig(
        filename="sw_planets_api.log",
        format="%(asctime)s:%(levelname)s:%(message)s",
        encoding="utf-8",
        level=logging.DEBUG
    )


def main() -> None:
    app = create_app()
    app.run(port=5000, host="localhost", debug=True)


if __name__ == "__main__":
    sys.exit(main())
