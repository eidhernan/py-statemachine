# py-statemachine
A module for creating simple yet effective object-oriented state machines, with transitions that include logic, and creating transitions is as easy as decorating a function.


Example of a "padlock" program:
```py 
from pystatemachine import State, StateMachine

padlock = StateMachine(initial_state = "LOCKED")
state_locked = State()
padlock["LOCKED"] = state_locked

@state_locked.transition
def unlock():
    print("Unlocking the lock...")
    return "UNLOCKED" 

state_unlocked = State()
padlock["UNLOCKED"] = state_unlocked

@state_unlocked.transition
def lock():
    print("Locking the lock...")
    return "LOCKED"

if __name__ == "__main__":
    print(f"State of 'padlock': {padlock.state}")
    padlock("UNLOCK")
    print(f"State of 'padlock': {padlock.state}")
```

If you take your time and read the code, I am sure you can figure out how it works. That is just a simple program, but we can go really advanced.
