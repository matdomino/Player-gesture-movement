import json
import os

config_path = os.path.abspath("./config/config.json")
default_path = os.path.abspath("./config/default.json")

def read_config():
    with open(config_path) as f:
        config = json.load(f)

    return config
