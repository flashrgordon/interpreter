from State import State

class FSM:
    states = []
    alphabet = []
    delta = [[],[],[]]  # [[from state],[transition symbol],[to state]]
    initial: State = None
    accepting = []

    ### Constructors ###
    # default
    def __init__(self):   # default FSM accepts only the empty string
        q0 = State()  # q1 is the initial and accepting state with no transitions
        self.states = [q0]  # q1 is the only state
        self.alphabet = []
        self.delta = [[], [], []]
        self.initial = q0
        self.accepting = [q0]

    # parameterized
    def __init__(self, Q, sigma, delta, q0, q_acc):
        self.states = Q
        self.alphabet = sigma
        self.delta = delta
        self.initial = q0
        self.accepting = q_acc
        
