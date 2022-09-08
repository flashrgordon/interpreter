from State import State

class FSM:
    states = [] # list of state objects (not indices)
    alphabet = []   # list of alphabet strings (sigma)
    delta = [[],[],[]]  # [[from state (index)],[transition symbol (str)],[to state (index)]]
    initial: State = None    # single initial state (index)
    accepting = []   # list of accepting state (indices)


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


    def addState(self, accepting, transitions):    # transitions should be [[transition symbol (str)], [to state (index)]]
        index = len(self.states)
        initial = (len(self.states) == 0)  # this is the first state being added to the FSM if there are no states in self,states

        state = State(index, accepting, initial, transitions)
        self.states.append(state)
        if (accepting):
            self.accepting.append(index)
        if initial:
            self.initial = initial

        # we do not handle transitions when states are added, all states must be added before transitions are implemented!!!


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


    def addAlphabet(self, a):
        self.alphabet = a

    