from file import File
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

file = File()
pokemon_list = file.load_data()


class PokemonList(Resource):
    def get(self):
        """
        Returns json of all pokemon
        :return: json
        """
        return {"pokemon": pokemon_list}, 200


class Pokemon(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "id",
        type=int,
        required=True,
        location="json",
        help="This field cannot be left blank!",
    )
    parser.add_argument("type1", type=str, required=True, location="json")
    parser.add_argument("type2", type=str, required=True, location="json")
    parser.add_argument("total", type=str, required=True, location="json")
    parser.add_argument("HP", type=str, required=True, location="json")
    parser.add_argument("attack", type=str, required=True, location="json")
    parser.add_argument("defense", type=str, required=True, location="json")
    parser.add_argument("sp_atk", type=str, required=True, location="json")
    parser.add_argument("sp_def", type=str, required=True, location="json")
    parser.add_argument("speed", type=str, required=True, location="json")
    parser.add_argument("gen", type=str, required=True, location="json")
    parser.add_argument("legend", type=bool, required=True, location="json")

    def get(self, name: str):
        """
        Returns json of a specific pokemon by name
        :param name: string
        :return: json
        """
        pokemon = next(
            filter(lambda x: x["name"] == name, pokemon_list), None
        )
        return (
            {"pokemon": pokemon},
            200 if pokemon else 404,
        )  # Not Found Error

    def delete(self, name: str):
        global pokemon_list  # outside of method
        pokemon_list = list(filter(lambda x: x["name"] != name, pokemon_list))
        return {"message": "item deleted"}, 200

    def post(self, name: str):
        """
        Post new pokemon to pokemon_list
        :param name: str
        :return: updated pokemon_list
        """
        if next(filter(lambda x: x["name"] == name, pokemon_list), None):
            return {
                "message": "An Pokemon with name '{}' already exists".format(
                    name
                )
            }
        data = Pokemon.parser.parse_args()
        pokemon = self.__create_pokemon(data, name)
        pokemon_list.append(pokemon)
        return pokemon, 201

    def put(self, name: str):
        """
        Post new pokemon to pokemon_list or update if pokemon
        already exists
        :param name: str
        :return: updated pokemon_list
        """
        data = Pokemon.parser.parse_args()
        pokemon = next(
            filter(lambda x: x["name"] == name, pokemon_list), None
        )
        if pokemon is None:
            pokemon = self.__create_pokemon(data, name)
            pokemon_list.append(pokemon)
            return pokemon, 201
        else:
            pokemon.update(data)
        return pokemon, 200

    @staticmethod
    def __create_pokemon(data: dict, name: str) -> dict:
        """
        creates a pokemon
        :param data: json args from user (dict)
        :param name: str - pokemon name
        :return: updated dict
        """
        pokemon = {
            "id": data["id"],
            "name": name,
            "type1": data["type1"],
            "type2": data["type2"],
            "total": data["total"],
            "HP": data["HP"],
            "attack": data["attack"],
            "defense": data["defense"],
            "sp_atk": data["sp_atk"],
            "sp_def": data["sp_def"],
            "speed": data["speed"],
            "gen": data["gen"],
            "legend": data["legend"],
        }
        return pokemon


api.add_resource(PokemonList, "/pokemon/")
api.add_resource(Pokemon, "/pokemon/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
