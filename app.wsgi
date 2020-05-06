# flake8: noqa
activate_this = "/home/ubuntu/PokemonAPI/venv/bin/activate_this.py"
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

import logging
import sys

from app import app as application

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/PokemonAPI/")
