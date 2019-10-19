import os
import json

config = None


def init_config():
    global config
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')) as f:
        config = json.load(f)


init_config()