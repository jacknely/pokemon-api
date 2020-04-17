![Python application](https://github.com/jacknely/PokemonAPI/workflows/Python%20application/badge.svg)
![Python package](https://github.com/jacknely/PokemonAPI/workflows/Python%20package/badge.svg)
![Docker Image CI](https://github.com/jacknely/PokemonAPI/workflows/Docker%20Image%20CI/badge.svg)



# PokemonAPI
PokemonAPI for managing Pokemon. Performs a set of operations on an imported Pokemon file.
Allows you to POST, PUT, GET & DELETE a Pokemon by name.

## Requirements

- Python 3.7
- Flask


Install from requirements.txt


## Usage

Running the web app.

```
set FLASK_APP=run.py
flask run
```
Navigate to local host with Pokemon name in order to see details of all Pokemon in application.
```
http://127.0.0.1:5000/pokemon
```
### Get All Pokemon

Navigate to the below address.

```
http://127.0.0.1:5000/pokemon
```
### Get Specific Pokemon

GET Pokemon by replacing <name> in following address:
```
http://127.0.0.1:5000/pokemon/<name>
```
  
### Add New Pokemon
  
Add a Pokemon using a POST request with the data to be added for the new <name> in json format in body.

```
http://127.0.0.1:5000/pokemon/<name>
```
```
{	
  "HP": "str",
  "attack": "str",
  "defense": "str",
  "gen": "str",
  "legend": "str",
  "sp_atk": "str",
  "sp_def": "str",
  "speed": "str",
  "total": "str",
  "type1": "str",
  "type2": "str",
  "id": "int"
}
```

### Update Specific Pokemon
  
Update existing Pokemon using a PUT or POST request with the data to be updated for the corresponding <name> in json format in body.

```
http://127.0.0.1:5000/pokemon/<name>
```
```
{	
  "HP": "str",
  "attack": "str",
  "defense": "str",
  "gen": "str",
  "legend": "str",
  "sp_atk": "str",
  "sp_def": "str",
  "speed": "str",
  "total": "str",
  "type1": "str",
  "type2": "str",
  "id": "int"
}
```
### Delete Specific Pokemon
  
Delete existing Pokemon using a DELETE request with the corresponding <name> in address.

```
http://127.0.0.1:5000/pokemon/<name>
```
  
  
