import json


_config = None


def get_config():
    global _config
    if not _config:
        with open('env.json', 'r') as f:
            _config = json.load(f)
    return _config
