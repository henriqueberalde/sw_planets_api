import sys
import logging
from app import create_app
from flasgger import Flasgger, Swagger

logging.basicConfig(
        filename="sw_planets_api.log",
        format="%(asctime)s:%(levelname)s:%(message)s",
        encoding="utf-8",
        level=logging.DEBUG
    )


def main() -> None:
    app = create_app()

    s = Swagger(app)
    app.run(port=5005, host="0.0.0.0", debug=True)


if __name__ == "__main__":
    sys.exit(main())
