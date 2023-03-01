import requests
from sw_planets_api.models.planet import Planet, Film


class StarWarsApiService:
    @staticmethod
    def load_planet(session, id) -> Planet:
        url = "https://swapi.dev/api/planets/{}".format(id)

        response = requests.get(url)
        data = response.json()

        if data is None:
            raise Exception(f"Error on getting planet by id {id}. Please check id number again on https://swapi.dev/")  # nopep8

        if data.get("detail") == "Not found":
            raise Exception(f"Planet {id} not found on star wars api. Please check id number again on https://swapi.dev/")  # nopep8

        planet = Planet.from_json(session, data, id)

        films = []
        films_filed = data.get("films")
        if films_filed is not None:
            for film_url in films_filed:
                films.append(StarWarsApiService.load_film(session, film_url))

        planet.films = films

        return planet

    @staticmethod
    def load_film(session, url) -> Film:
        id = url.replace("https://swapi.dev/api/films/", "").replace("/", "")

        response = requests.get(url)
        data = response.json()

        if data is None:
            raise Exception(f"Error on getting film by url {url}.")  # nopep8

        return Film.from_json(session, data, int(id))
