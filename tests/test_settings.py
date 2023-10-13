import unittest
import model
import os


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.settings = model.Settings()
        if os.path.exists("config.ini"):
            os.remove("config.ini")

    def test_create_load(self):
        config1 = model.create_settings()
        config2 = model.load_settings()
        for section in config1:
            for key in config1[section]:
                self.assertEqual(config1[section][key], config2[section][key],
                                 "created config is not equal to same config after loading")

    def test_update_load(self):
        config1 = model.create_settings()
        config1["TAPE_SETTINGS"]["amount_tapes"] = "2"
        model.update_settings(config1)
        config2 = model.load_settings()
        for section in config1:
            for key in config1[section]:
                self.assertEqual(config1[section][key], config2[section][key],
                                 "updated config is not equal to same config after loading")

    def test_is_singleton(self):
        self.other_settings = model.Settings()
        self.other_settings.set_setting("TAPE_SETTINGS", "amount_tapes", "2")
        self.assertEqual(self.settings.get_setting("TAPE_SETTINGS", "amount_tapes"),
                         self.other_settings.get_setting("TAPE_SETTINGS", "amount_tapes"),
                         "singleton settings class can have multiple instances")


if __name__ == '__main__':
    unittest.main()
