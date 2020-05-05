# py-statemachine
A module for creating simple yet effective state machines, with transitions that include logic, and creating transitions is as easy as decorating a function.


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

But first, let's go into actually creating a state machine from the beginning. To a create a new state machine instance, simply create an instance of ``StateMachine``. For this example, we are going to be using a padlock example, with there being two states, ``LOCKED``, and ``UNLOCKED``.

```py
from pystatemachine import State, StateMachine

padlock = StateMachine("LOCKED") # "LOCKED" is the initial state for the StateMachine to be in.
```
You may notice a parameter for ``StateMachine``, "LOCKED". This is the ``initial_state`` parameter, it is a default state for the ``StateMachine`` to be in upon creation. Without this parameter, the ``StateMachine`` will be in no state at all, and will raise an error.

```diff
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    padlock = StateMachine()
TypeError: __init__() missing 1 required positional argument: 'initial_state'
```
So with that, we can add some states. You know how we created an initial state, ``LOCKED``? Well, we didn't actually *create* that state, we just made a pointer for it. An identifier, so the StateMachine knows where to start. We still have to declare it as a state though.
