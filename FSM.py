from State import State

class FSM:
    states = [] # list of state objects (not indices)
    alphabet = []   # list of alphabet strings (sigma)
    delta = [[],[],[]]  # [[from state (index)],[transition symbol (str)],[to state (index)]]
    initial: State = None    # single initial state
    accepting = []   # list of accepting states


    ### Constructors ###
    # default
    def __init__(self):   # default FSM accepts no strings
        print('Empty FSM instantiated.')

    # parameterized
    def __init__(self, Q, sigma, delta, q0, q_acc):
        self.states = Q
        self.alphabet = sigma
        self.delta = delta
        self.initial = q0
        self.accepting = q_acc


    def addState(self, accepting, initial, transitions):    # transitions should be [[transition symbol (str)], [to state (index)]]
        state = State(len(self.states), accepting, initial, transitions)

    def addTransitions(self):   # transitions must be added after all states in Q to avoid transitions to nonexistent states
        for i in self.states:
            transitions = i.getTransitions()
            if (len(transitions[0]) > 0):
                for j in range(len(transitions[0])):
                    self.delta[0].append(i.getIndex())   # from state index
                    self.delta[1].append(transitions[0][j])     # transition symbol
                    self.delta[2].append(transitions[1][j])      # to state index



    def getStateByIndex(self, i):
        if (i > 0):
            return self.states[i-1]
        else:
            return None