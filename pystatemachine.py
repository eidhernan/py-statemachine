class StateMachine:
    """A state machine object."""
    def __init__(self, initial_state = "DEFAULT"):
        self.state = initial_state
        self.states = {}
        
    def __repr__(self):
        return repr(self.state)
    
    def __call__(self, transition):
        """The __call__() method is a trigger for state transitions."""
        new = self.states[self.state].transitions[transition]() # Execute the transition, storing the return state value.
        if new in self.states.keys(): # Checks whether or not the state returned from the transition is declared in self.states
            self.state = new # Change the state to the one specified in the transition
        else:
            raise ValueError(new)
    def __getitem__(self, item):
        """Used for ease in looking up states"""
        return self.states[item]

    def __setitem__(self, item, value):
        """Used for ease to set states"""
        self.states[item] = value

class Transition:
    """Transition objects, used to transition between 2 states with logic"""
    def __init__(self, func):
        self.func = func # The function to use when transitioning between states.
    
    def __call__(self):
        """Stimulates self.func()"""
        return self.func()

class State:
    """A concrete state for a StateMachine instance. These states have no logic, but their transitions do"""
    def __init__(self):
        self.transitions = {} # Create an empty dictionary to represent transitions for this state

    def transition(self, func):
        """Wizard to create transitions out of functions"""
        self.transitions[func.__name__.upper()] = Transition(func) # Creates a transition, and stores it into self.transitions
        return func
