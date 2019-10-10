from flask import Flask
from flask_restful import Resource, Api
from load_pokemon import *

app = Flask(__name__)
api = Api(app)

pokemon = import_json()


class Pokemon(Resource):
    def get(self):
        """
        Returns json of all pokemon
        :return:
        """
        return pokemon


api.add_resource(Pokemon, '/pokemon/')

app.run(debug=True)
