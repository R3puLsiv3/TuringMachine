import unittest
import model


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # TODO: Load a turing machine once functionality exists
        transitions0 = [model.Transition(0, "0", "0", "1", "R", "1"), model.Transition(0, "0", "1", "0", "N", "0"),
                        model.Transition(0, "0", " ", "1", "L", "0")]

        transitions1 = [model.Transition(0, "1", "0", "0", "R", "0"), model.Transition(0, "1", "1", " ", "R", "1"),
                        model.Transition(0, "1", " ", "1", "L", "1")]

        states = [model.State("0", False, transitions0), model.State("1", False, transitions1)]

        self.tm = model.TuringMachine(states)

    def test_get_tape_alphabet(self):
        self.assertSetEqual(self.tm.get_tape_alphabet(), {" ", "0", "1"}, "incorrect tape alphabet")

    def test_get_input_alphabet(self):
        self.assertSetEqual(self.tm.get_input_alphabet(), {"0", "1"}, "incorrect input alphabet")


if __name__ == '__main__':
    unittest.main()
