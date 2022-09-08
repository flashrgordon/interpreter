class State:
    index: int = 0
    accepting = False
    initial = False
    transitions = [[], []]  # [[transition symbol (str)], [to state (index)]]

    ### Constructors ###
    # default
    def __init__(self):
        self.index = 1
        self.accepting = True
        self.initial = True
        transitions = [[], []]

    # parameterized
    def __init__(self, index, accepting, initial, transitions):
        self.index = index
        self.accepting = accepting
        self.initial = initial
        self.transitions = transitions




    def getIndex(self):
        return self.index

    def getTransitions(self):
        return self.transitions