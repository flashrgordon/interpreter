from re import L
from this import d


from FSM import FSM

class Regex:
    language = []
    FSM: Object = None

    def setLanguage(self, l):
        self.language = l

    def generateFSM(self):
