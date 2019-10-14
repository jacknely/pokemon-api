from flask import Flask, request
from flask_restful import Resource, Api
from load_pokemon import *

app = Flask(__name__)
api = Api(app)

pokemon_list = []  # import_json()


class PokemonList(Resource):
    def get(self):
        """
        Returns json of all pokemon
        :return: json
        """
        return {"pokemon": pokemon_list}, 200


class Pokemon(Resource):
    def get(self, name: str):
        """
        Returns json of a specific pokemon by name
        :param name: string
        :return: json
        """
        pokemon = next(filter(lambda x: x['name'] == name, pokemon_list), None)
        return {'pokemon': pokemon}, 200 if pokemon else 404  # Not Found Error

    def delete(self, name: str):
        global pokemon  # outside
        pokemon = list(filter(lambda x: x['name'] != name, pokemon))
        return {'message': 'item deleted'}, 200

    def post(self, name: str):
        """
        Post new pokemon to pokemon_list
        :param name: str
        :return: updated pokemon_list
        """
        if next(filter(lambda x: x['name'] == name, pokemon_list), None):
            return {'message': "An Pokemon with name '{}' already exists".format(name)}

        data = request.get_json()
        pokemon = self.create_pokemon(data, name)
        pokemon_list.append(pokemon)
        return pokemon, 201

    def put(self, name: str):
        """
        Post new pokemon to pokemon_list or update if pokemon
        already exists
        :param name: str
        :return: updated pokemon_list
        """
        data = request.get_json()
        pokemon = next(filter(lambda x: x['name'] == name, pokemon_list), None)
        if pokemon is None:
            pokemon = self.create_pokemon(data, name)
            pokemon_list.append(pokemon)
            return pokemon, 201
        else:
            pokemon.update(data)
        return pokemon

    @staticmethod
    def create_pokemon(data: dict, name: str) -> dict:
        """

        :param data: json args from user (dict)
        :param name: str - pokemon name
        :return: updated dict
        """
        pokemon = {
            "id": data['id'],
            "name": name,
            "type1": data['type1'],
            "type2": data['type2'],
            "total": data['total'],
            "HP": data['HP'],
            "attack": data['attack'],
            "defense": data['defense'],
            "sp_atk": data['sp_atk'],
            "sp_def": data['sp_def'],
            "speed": data['speed'],
            "gen": data['gen'],
            "legend": data['legend']
        }
        return pokemon


api.add_resource(PokemonList, '/pokemon/')
api.add_resource(Pokemon, '/pokemon/<string:name>')

app.run(debug=True)
