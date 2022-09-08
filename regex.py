from re import L
from this import d


from FSM import FSM

class Regex:
    alphabet = []
    machine: FSM = None

    ### Constructor ###
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.machine.setAlphabet(alphabet)