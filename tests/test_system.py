from pathlib import Path
from unittest.mock import patch

import pytest
from app import app
from file import File


@pytest.fixture(scope="session")
def client():
    test_client = app.test_client()
    yield test_client


@pytest.fixture
def test_pokemon():
    test_data = {
        "HP": "TTT",
        "attack": "TTT",
        "defense": "TTT",
        "gen": "TTT",
        "legend": "False",
        "sp_atk": "TTT",
        "sp_def": "TTT",
        "speed": "TTT",
        "total": "TTT",
        "type1": "TTT",
        "type2": "TTT",
        "id": "444",
    }
    return test_data


class TestFile:
    def setup_method(self):
        test_json = f"{Path(__file__).parent}/test_data.json"
        test_file = File()
        self.pokemon_list = test_file.import_json(test_json)

    def test_get_pokemonlist(self, client):
        response = client.get("/pokemon/")

        assert response.status_code == 200
        assert b"Bulbasaur" in response.data

    def test_get_pokemon(self, client):
        response = client.get("/pokemon/Bulbasaur")

        assert response.status_code == 200
        assert b"Bulbasaur" in response.data

    def test_delete_pokemon(self, client):
        response = client.delete("/pokemon/Bulbasaur")

        assert response.status_code == 200
        assert b"deleted" in response.data

    def test_post_pokemon(self, client, test_pokemon):
        with patch("flask_restful.reqparse.RequestParser.parse_args",) as m:
            m.return_value = test_pokemon
            response = client.post("/pokemon/poke", data=test_pokemon)

        assert response.status_code == 201
        assert b"poke" in response.data

    def test_put_pokemon(self, client, test_pokemon):
        with patch("flask_restful.reqparse.RequestParser.parse_args",) as m:
            m.return_value = test_pokemon
            response = client.put("/pokemon/poke2", data=test_pokemon)

        assert response.status_code == 201
        assert b"poke" in response.data
