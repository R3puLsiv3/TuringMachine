
class Transition:

    def __init__(self, tape: int, old_state: str, read: str, write: str, movement: str, new_state: str):
        self.tape = tape
        self.old_state = old_state
        self.read = read
        self.write = write
        self.movement = movement
        self.new_state = new_state
