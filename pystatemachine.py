class StateMachine:
    def __init__(self, initial_state = "DEFAULT"):
        self.state = initial_state
        self.states = {}

    def __call__(self, transition):
        new = self.states[self.state].transitions[transition]()
        if new in self.states.keys():
            self.state = new
        else:
            raise ValueError(new)
    def __getitem__(self, item):
        return self.states[item]

    def __setitem__(self, item, value):
        self.states[item] = value

class Transition:
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        return self.func()

class State:
    def __init__(self):
        self.transitions = {}

    def transition(self, func):
        """Wizard to create transitions out of functions"""
        self.transitions[func.__name__.upper()] = Transition(func)
        return func
