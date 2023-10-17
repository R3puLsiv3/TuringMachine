from configparser import ConfigParser

CONFIG_PATH = "config.ini"


def create_settings() -> dict:
    config = ConfigParser()

    config["WINDOW_SETTINGS"] = {
        "width": 1080,
        "height": 720,
        "pos_x": 0,
        "pos_y": 0,
        "full-screen": 0
    }

    config["TAPE_SETTINGS"] = {
        "blank_symbol": "EMPTY",
        "amount_tapes": 1
    }

    with open(CONFIG_PATH, "w") as conf:
        config.write(conf)
    return config_to_dict(config)


def load_settings() -> dict:
    config = ConfigParser()
    config.read(CONFIG_PATH)
    if config.read(CONFIG_PATH):
        return config_to_dict(config)
    return create_settings()


def config_to_dict(config: ConfigParser) -> dict:
    try:
        settings_dict = {"width": int(config["WINDOW_SETTINGS"]["width"]),
                         "height": int(config["WINDOW_SETTINGS"]["height"]),
                         "pos_x": int(config["WINDOW_SETTINGS"]["pos_x"]),
                         "pos_y": int(config["WINDOW_SETTINGS"]["pos_y"]),
                         "full-screen": bool(int(config["WINDOW_SETTINGS"]["full-screen"])),
                         "blank_symbol": config["TAPE_SETTINGS"]["blank_symbol"],
                         "amount_tapes": int(config["TAPE_SETTINGS"]["amount_tapes"])}
    except ValueError:
        print("Loaded corrupted config file. Recreating base config.")
        return create_settings()

    return settings_dict


def dict_to_config(_dict: dict) -> ConfigParser:
    config = ConfigParser()

    config["WINDOW_SETTINGS"] = {
        "width": _dict["width"],
        "height": _dict["height"],
        "pos_x": _dict["pos_x"],
        "pos_y": _dict["pos_y"],
        "full-screen": _dict["full-screen"]
    }

    config["TAPE_SETTINGS"] = {
        "blank_symbol": _dict["blank_symbol"],
        "amount_tapes": _dict["amount_tapes"]
    }

    return config


def update_settings(settings):
    config = dict_to_config(settings)

    with open(CONFIG_PATH, "w") as conf:
        config.write(conf)


class Settings(object):

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Settings, cls).__new__(cls)

            cls.instance.settings = load_settings()

        return cls.instance
