import model
import re

TRANSITION_REGEX = re.compile("([^,|]|blank|div|comma)(\|([^,|]|blank|div|comma))*"
                              "->([^,|]|blank|div|comma)(\|([^,|]|blank|div|comma))*,[LRN](\|[LRN])*,.+")


def parse_transitions(transitions: str):
    parsed_transitions: list[model.Transition] = []
    split_transitions = transitions.splitlines()
    for transition in split_transitions:
        transition = transition.replace(" ", "")
        if TRANSITION_REGEX.fullmatch(transition):
            read_split = transition.split("->", 1)
            read = read_split[0].split("|")
            for i in range(len(read)):
                match read[i]:
                    case "blank":
                        read[i] = model.turing_machine.BLANK_SYMBOL
                    case "div":
                        read[i] = "|"
                    case "comma":
                        read[i] = ","

            write_split = read_split[1].split(",", 1)
            write = write_split[0].split("|")
            for i in range(len(write)):
                match write[i]:
                    case "blank":
                        write[i] = model.turing_machine.BLANK_SYMBOL
                    case "div":
                        write[i] = "|"
                    case "comma":
                        write[i] = ","

            if len(read) != len(write):
                raise ValueError

            movement_split = write_split[1].split(",", 1)
            movement = movement_split[0].split("|")

            if len(movement) != len(write):
                raise ValueError

            new_state = movement_split[1]

            parsed_transitions.append(model.Transition(read, write, movement, new_state))
        elif not transition:
            continue
        else:
            raise ValueError
    return parsed_transitions


def reverse_parse_transitions(transitions) -> str:
    transition_str = ""

    for transition in transitions:
        read_str = ""
        for symbol in transition.read:
            match symbol:
                case model.turing_machine.BLANK_SYMBOL:
                    read_str += "blank" + "|"
                case "|":
                    read_str += "div" + "|"
                case ",":
                    read_str += "comma" + "|"
                case _:
                    read_str += symbol + "|"

        write_str = ""
        for symbol in transition.write:
            match symbol:
                case model.turing_machine.BLANK_SYMBOL:
                    write_str += "blank" + "|"
                case "|":
                    write_str += "div" + "|"
                case ",":
                    write_str += "comma" + "|"
                case _:
                    write_str += symbol + "|"

        movement_str = ""
        for symbol in transition.movement:
            movement_str += symbol + "|"

        transition_str += read_str[:-1] + "->" + write_str[:-1] + "," + movement_str[:-1] + "," + transition.new_state + "\n"
    return transition_str[:-1]


class Transition:
    def __init__(self, read: list[str], write: list[str], movement: list[str], new_state: str):
        self.read = read
        self.write = write
        self.movement = movement
        self.new_state = new_state
