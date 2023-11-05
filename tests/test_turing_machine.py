import unittest
import model


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # TODO: Load a turing machine once functionality exists
        transitions0 = [model.Transition(0, "0", "1", "R", "1"), model.Transition(0, "1", "0", "N", "0"),
                        model.Transition(0, " ", "1", "L", "0")]

        transitions1 = [model.Transition(0, "0", "0", "R", "0"), model.Transition(0, "1", " ", "R", "1"),
                        model.Transition(0, " ", "1", "L", "1")]

        states = {"0": model.State(True, transitions0), "1": model.State(False, transitions1)}

        self.tm = model.TuringMachine(states)

    def test_get_tape_alphabet(self):
        self.assertSetEqual(self.tm.get_tape_alphabet(), {" ", "0", "1"}, "incorrect tape alphabet")

    def test_get_input_alphabet(self):
        self.assertSetEqual(self.tm.get_input_alphabet(), {"0", "1"}, "incorrect input alphabet")

    def test_get_halting_states(self):
        self.assertSetEqual(self.tm.get_halting_states(), {"0"}, "incorrect halting states")


if __name__ == '__main__':
    unittest.main()
