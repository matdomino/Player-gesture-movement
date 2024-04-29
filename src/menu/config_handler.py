import json
import os

config_path = os.path.abspath("./config/config.json")
default_path = os.path.abspath("./config/default.json")

def read_config():
    with open(config_path) as f:
        config = json.load(f)

    return config

def restore_to_default():
    with open(default_path) as f:
        default_config = json.load(f)

    with open(config_path, 'w') as f:
        json.dump(default_config, f, indent=4)

def save_config(config):
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
