class State:
    index: int = 0
    accepting = False
    initial = False

    ### Constructors ###
    # default
    def __init__(self):
        self.index = 1
        self.accepting = True
        self.initial = True

    # parameterized
    def __init__(self, index, accepting, initial):
        self.index = index
        self.accepting = accepting
        self.initial = initial