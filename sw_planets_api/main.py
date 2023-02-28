import sys
import logging
import mysql.connector
# from sw_planets_api.Planet import Planet


logging.basicConfig(filename="sw_planets_api.log",
                    format="%(asctime)s:%(levelname)s:%(message)s",
                    encoding="utf-8",
                    level=logging.DEBUG)


def main() -> None:
    connection = mysql.connector.connect(
        user="root",
        password="root",
        host="sw_planets_db",
        port="3306",
        database="db"
    )
    print("DBN connected")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM planets")
    planets = cursor.fetchall()
    connection.close()

    print(planets)


if __name__ == "__main__":
    sys.exit(main())
