import sys
import logging
from sw_planets_api.Planet import Planet


logging.basicConfig(filename="sw_planets_api.log",
                    format="%(asctime)s:%(levelname)s:%(message)s",
                    encoding="utf-8",
                    level=logging.DEBUG)


def main() -> None:
    p = Planet()
    logging.info("Printing Planet.test()")
    print(p.test())


if __name__ == "__main__":
    sys.exit(main())
