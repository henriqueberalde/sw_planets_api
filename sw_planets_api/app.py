import sw_planets_api.models.db as db

from flask import Flask, jsonify, request
from sw_planets_api.models.planet import Planet
from sw_planets_api.services.star_wars_api_service import StarWarsApiService
from logging.config import dictConfig
from sqlalchemy.orm.util import object_state


def response_obj(data, error):
    if error is None:
        success = True
    elif str(error) == "":
        success = True
    else:
        success = False

    return jsonify({
        "data": data,
        "error": error,
        "success": success
    })


def create_app(session=None):
    if session is None:
        session = db.get_session()

    dictConfig({
        "version": 1,
        "formatters": {"default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }},
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default"
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "sw_planets_api.log",
                "formatter": "default"
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["wsgi", "file"]
        }
    })

    app = Flask(__name__)

    @app.route("/planets/load/<int:id>", methods=["POST"])
    def insert_planet_from_api(id):
        planet = StarWarsApiService.load_planet(session, id)

        app.logger.info(f"Planet {planet.name} loaded from SWAPI.")

        if not object_state(planet).persistent:
            session.add(planet)
            session.commit()
            app.logger.info(f"Planet {planet.name} inserted on db")  # nopep8
        else:
            app.logger.info(f"Planet {planet.name} already exists on db")  # nopep8

        return response_obj(planet.serialize(), None)

    @app.route("/planets", methods=["GET"])
    def get_planets():
        args = request.args

        if len(args) > 0:
            app.logger.info(f"Searching planets by {args}")
            planets = session.query(Planet).filter_by(**args).all()
        else:
            app.logger.info("Searching all planets")
            planets = session.query(Planet).all()

        return response_obj([p.serialize() for p in planets], None)

    @app.route("/planets/<int:id>", methods=["GET"])
    def get_planet_by_id(id: int):
        app.logger.info(f"Getting planet {id}")
        planet = session.get(Planet, id)

        return response_obj(planet.serialize(), None)

    @app.route("/planets/<int:id>", methods=["DELETE"])
    def remove_planet(id: int):
        app.logger.info(f"Removing planet {id}")
        planet = session.get(Planet, id)

        session.delete(planet)
        session.commit()

        return response_obj(None, None)

    @app.errorhandler(Exception)
    def handle_sqlalchemy_assertion_error(err):
        msg = str(err)
        app.logger.error(msg)
        return response_obj(None, msg)

    return app
