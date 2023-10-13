import unittest
import model


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.tm = model.TuringMachine()
        self.tm.states.append({"1": ["2", "L", 2], "2": ["b", "N", 3], "_": ["2", "R", 1]})
        self.tm.states.append({"1": ["1", "R", 3], "2": ["_", "R", 3], "_": ["_", "L", 2]})
        self.tm.states.append({"1": ["c", "L", 1], "2": ["2", "N", 1], "_": ["a", "N", 3]})

    def test_get_tape_alphabet(self):
        self.assertSetEqual(self.tm.get_tape_alphabet(), {"_", "1", "2", "a", "b", "c"}, "incorrect tape alphabet")

    def test_get_input_alphabet(self):
        self.assertSetEqual(self.tm.get_input_alphabet(), {"1", "2"}, "incorrect input alphabet")


if __name__ == '__main__':
    unittest.main()
