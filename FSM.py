from State import State

class FSM:
    states = []
    alphabet = []
    delta = [[],[],[]]  # [[from state],[transition symbol],[to state]]
    initial: State = None
    accepting = []