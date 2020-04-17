import csv
import json
import os
from pathlib import Path


class File:
    def load_data(self):
        json_file = f"{Path(__file__).parent}/pokemon.json"
        csv_file = f"{Path(__file__).parent}/pokemon.csv"
        try:
            pokemon_data = self.import_json(json_file)
        except FileNotFoundError:
            pokemon_data = self.import_csv_as_json(csv_file)
            self.export_json(json_file, pokemon_data)

        return pokemon_data

    @staticmethod
    def import_csv_as_json(filepath: str) -> list:
        """
        imports pokemon from csv file
        :return: pokemon data in dict/json format
        """
        csv_file = open(filepath, "r")
        fieldnames = (
            "id",
            "name",
            "type1",
            "type2",
            "total",
            "HP",
            "attack",
            "defense",
            "sp_atk",
            "sp_def",
            "speed",
            "gen",
            "legend",
        )
        reader = csv.DictReader(csv_file, fieldnames)
        pokemon_import = []
        next(reader)  # skip first row of headers
        for row in reader:
            pokemon_import.append(row)
        return pokemon_import

    @staticmethod
    def export_json(filename, pokemon_data):
        """
        exports pokemon data to json file
        :param filename:
        :param pokemon_data: dict
        :return: save json file
        """
        with open(filename, "w") as file:
            file.write(json.dumps(pokemon_data))

    @staticmethod
    def import_json(filename) -> dict:
        """
        import pokemon data from json file
        :return: pokemon data in dict/json format
        """
        with open(filename, "r") as f:
            pokemon_import = json.load(f)
        return pokemon_import
