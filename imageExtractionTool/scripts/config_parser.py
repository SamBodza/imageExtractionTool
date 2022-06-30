from configparser import ConfigParser


def get_config():
    config_object = ConfigParser()
    config_object.read("../scripts/config.ini")

    return config_object
