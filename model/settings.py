from configparser import ConfigParser

CONFIG_PATH = "config.ini"


def create_settings():
    config = ConfigParser()

    config["WINDOW_SETTINGS"] = {
        "width": "1920",
        "height": "1080"
    }

    config["TAPE_SETTINGS"] = {
        "blank_symbol": "EMPTY",
        "amount_tapes": "1"
    }

    with open(CONFIG_PATH, "w") as conf:
        config.write(conf)
    return config


def load_settings():
    config = ConfigParser()
    config.read(CONFIG_PATH)
    if config.read(CONFIG_PATH):
        return config

    return None


def update_settings(config):

    with open(CONFIG_PATH, "w") as conf:
        config.write(conf)


class Settings(object):

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Settings, cls).__new__(cls)

            cls.instance.settings = load_settings()
            if cls.instance.settings is None:
                cls.instance.settings = create_settings()

        return cls.instance

    def get_setting(self, setting_type: str, setting: str):
        return self.settings[setting_type][setting]

    def set_setting(self, setting_type: str, setting: str, value):
        self.settings[setting_type][setting] = value
