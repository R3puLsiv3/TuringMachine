import unittest
import model
import os


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.settings = model.Settings()
        if os.path.exists(model.CONFIG_PATH):
            os.remove(model.CONFIG_PATH)

    def tearDown(self):
        if os.path.exists(model.CONFIG_PATH):
            os.remove(model.CONFIG_PATH)


if __name__ == '__main__':
    unittest.main()
