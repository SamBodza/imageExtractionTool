from configparser import ConfigParser


def get_config():
    config_object = ConfigParser()
    try:
        config_object.read("../scripts/config.ini")
        test = config_object['PATHS']
    except Exception as e:
        config_object.read("./imageExtractionTool/scripts/config.ini")
        test = config_object['PATHS']

    return config_object
