
class Transition:

    def __init__(self, tape: int, read: str, write: str, movement: str, new_state: str):
        self.tape = tape
        self.read = read
        self.write = write
        self.movement = movement
        self.new_state = new_state
