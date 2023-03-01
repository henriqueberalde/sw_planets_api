import sw_planets_api.models.db as db

from flask import Flask, jsonify, request, make_response, Response
from sw_planets_api.models.planet import Planet
from sw_planets_api.services.star_wars_api_service import StarWarsApiService


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

    app = Flask(__name__)

    @app.route("/planets/load/<int:id>", methods=["POST"])
    def insert_planet_from_api(id):
        planet = StarWarsApiService.load_planet(session, id)

        if not planet.metadata.is_bound:
            session.add(planet)

        session.commit()

        return response_obj(planet.serialize(), None)

    @app.route("/planets", methods=["GET"])
    def get_planets():
        args = request.args

        if len(args) > 0:
            planets = session.query(Planet).filter_by(**args).all()
        else:
            planets = session.query(Planet).all()

        return response_obj([p.serialize() for p in planets], None)

    @app.route("/planets/<int:id>", methods=["GET"])
    def get_planet_by_id(id: int):
        planet = session.get(Planet, id)

        return response_obj(planet.serialize(), None)

    @app.route("/planets/<int:id>", methods=["DELETE"])
    def remove_planet(id: int):
        planet = session.get(Planet, id)

        session.delete(planet)
        session.commit()

        return response_obj(None, None)

    @app.errorhandler(Exception)
    def handle_sqlalchemy_assertion_error(err):
        return response_obj(None, str(err))

    return app
