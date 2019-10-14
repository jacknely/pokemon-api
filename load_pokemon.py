import csv
import json
import os


def import_csv_as_json() -> list:
    """
    imports pokemon from csv file
    :return: pokemon data in dict/json format
    """
    csv_file = open(os.path.realpath('pokemon.csv'), 'r')
    fieldnames = ("id", "name", "type1", "type2", "total", "HP", "attack", "defense", "sp_atk",
                  "sp_def", "speed", "gen", "legend")
    reader = csv.DictReader(csv_file, fieldnames)
    pokemon_import = []
    next(reader)  # skip first row of headers
    for row in reader:
        pokemon_import.append(row)
    return pokemon_import


def export_json(pokemon_data):
    """
    exports pokemon data to json file
    :param pokemon_data: dict
    :return: save json file
    """
    json_file = open(os.path.realpath('pokemon.json'), 'w')
    with json_file as f:
        f.write(json.dumps(pokemon_data))


def import_json() -> dict:
    """
    import pokemon data from json file
    :return: pokemon data in dict/json format
    """
    filename = os.path.realpath('pokemon.json')
    with open(filename, 'r') as f:
        pokemon_import = json.load(f)
    return pokemon_import


if __name__ == "__main__":
    pokemons = import_csv_as_json()
    export_json(pokemons)
    pokemons = import_json()
