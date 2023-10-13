from configparser import ConfigParser


def create_settings():
    config = ConfigParser()

    config["WINDOW_SETTINGS"] = {
    }

    config["TAPE_SETTINGS"] = {
        "blank_symbol": ""
    }

    with open("config.ini", "w") as conf:
        config.write(conf)
    return config


def load_settings():
    config = ConfigParser()
    config.read("config.ini")
    if config.read("config.ini"):
        return config

    return None


def update_settings(**settings):
    config = ConfigParser()
    pass


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
