import model
import re

TRANSITION_REGEX = re.compile("([1-9][0,9]*:)?.?->.?,[LRN],.+")


def parse_transitions(transitions: str):
    parsed_transitions: list[model.Transition] = []
    split_transitions = transitions.splitlines()
    for transition in split_transitions:
        transition = transition.replace(" ", "")
        transitions.lstrip("0")
        if TRANSITION_REGEX.fullmatch(transition):

            if transition[0].isdigit() and (transition[1].isdigit() or transition[1] == ":"):
                tape_split = transition.split(":", 1)
                tape = int(tape_split[0]) - 1
            else:
                tape_split = ["", transition]
                tape = 0

            if tape_split[1].startswith("->"):
                read = model.turing_machine.BLANK_SYMBOL
                rest = tape_split[1][2:]
            else:
                read = tape_split[1][0]
                rest = tape_split[1][3:]

            if rest[0] == "," and rest[1] != ",":
                write = model.turing_machine.BLANK_SYMBOL
                rest = rest[1:]
            else:
                write = rest[0]
                rest = rest[2:]

            movement = rest[0]
            new_state = rest[2:]

            # TODO: Remodel transitions to disallow for duplicate read possibility
            parsed_transitions.append(model.Transition(tape, read, write, movement, new_state))
        elif not transition:
            continue
        else:
            raise ValueError
    return parsed_transitions


def reverse_parse_transitions(transitions) -> str:
    transition_str = ""

    for transition in transitions:
        transition_str += str(transition.tape) + ":" + transition.read + "->" + transition.write + "," + \
                          transition.movement + "," + transition.new_state + "\n"
    return transition_str[:-1]


class Transition:

    def __init__(self, tape: int, read: str, write: str, movement: str, new_state: str):
        self.tape = tape
        self.read = read
        self.write = write
        self.movement = movement
        self.new_state = new_state
