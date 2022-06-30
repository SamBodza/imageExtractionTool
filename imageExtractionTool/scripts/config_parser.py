import os
from configparser import ConfigParser


def get_config():
    config_object = ConfigParser()
    try:
        path = os.path.join(os.path.dirname(__file__), "config.ini")
        config_object.read(path)
        test = config_object['PATHS']
    except Exception as e:
        config_object.read("./imageExtractionTool/scripts/config.ini")
        test = config_object['PATHS']

    return config_object
