import json
import os

config_path = os.path.abspath("./config/config.json")
default_path = os.path.abspath("./config/default.json")

def read_config() -> dict:
    """
    Loads keybinds and pointer configuration.

        Returns:
            - config (dict).
    """
    with open(config_path, encoding='utf-8') as f:
        config = json.load(f)

    return config
