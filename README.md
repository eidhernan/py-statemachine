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

# Creating a state machine

A state machine is any device storing the status of something at a given time. The status changes based on inputs, providing the resulting output for the implemented changes. 

In most state machines, there are concrete states, and transitions. Transitions are the drivers that change the device's state from one to another. We'll get to that, but first, we actually need to create one. We will be using a standard "traffic light" example.

```py
from pystatemachine import State, StateMachine

traffic_light = StateMachine("POWER_OFF")
```
As you can see, we can create state machines simply by invoking ``StateMachine``. You may also notice a parameter passed, ``"POWER_OFF"``. That parameter is the initial state that the device will be in. Without it, the ``StateMachine`` won't be in any state, and will be useless.

A traffic light is either off, or it has one of three lights on: red, yellow, or green. So we will need to create those states.

```py
power_off = State()

light_green = State()
light_yellow = State()
light_red = State()
```

Alright, now we have our state objects created, but they don't belong to our device, so we will need to do that. We can easily attach states to a state machine device using dictionary like item assignment, like so...

```py
traffic_light["POWER_OFF"] = power_off

traffic_light["LIGHT_GREEN"] = light_green
traffic_light["LIGHT_YELLOW"] = light_yellow
traffic_light["LIGHT_RED"] = light_red
```
And now these states are part of our finite state machine device, ``traffic_light``. We are almost done, we just need to create some transitions. A transition is a function like object, that details exactly how to transition from one state to another. The return value of a function defined for a transition, is the state to transition to. Think of it like this:

```
 [State 1]
     |
     V
[Transition]
     |
     V
 [State 2]
```

We can create a transition by simply using a decorator!

```py
@power_off.transition
def activate():
    print("Activating traffic light.")
    return "LIGHT_GREEN"
```
So why are we returning ``"LIGHT_GREEN"``? Because, that's the state we want to transition to. The next state is determined by the return value of the transition method. 

We can test this code by doing the following after:

```py
>>> traffic_light
    'POWER_OFF'
>>> traffic_light("ACTIVATE")
    Activating traffic light...
>>> traffic_light
    'LIGHT_GREEN'
```

As you can see, by calling ``traffic_light``, and passing in a transition name, encased in quotes, it triggers the transition. Transitions have the same name as the function, but in all caps.

Putting it all together, this is the final code. You may notice a ``time.sleep()`` in the transitions between lights, this is the "timer" for the lights, before it changes to a new light. Hopefully this tutorial will show you how capable state machines are, and feel free to extend this project, just make sure to credit me (=.

```py
from pystatemachine import State, StateMachine
from time import sleep

traffic_light = StateMachine("POWER_OFF")

power_off = State()
 
light_green = State()
light_yellow = State()
light_red = State()

traffic_light["POWER_OFF"] = power_off
 
traffic_light["LIGHT_GREEN"] = light_green
traffic_light["LIGHT_YELLOW"] = light_yellow
traffic_light["LIGHT_RED"] = light_red

@power_off.transition
def activate():
    print("Activating traffic light...")
    return "LIGHT_GREEN"

@light_green.transition
def switch():
    sleep(17) # Wait 17 seconds before transitioning to next state.
    return "LIGHT_YELLOW"

@light_yellow.transition
def switch():
    sleep(4) # Wait 4 seconds before transitioning to next state.
    return "LIGHT_RED"

@light_red.transition
def switch():
    sleep(17) # Wait 17 seconds before transitioning to next state.
    return "LIGHT_GREEN"

if __name__ == "__main__":
    traffic_light("ACTIVATE")
    while True:
        print(f"Current State: {traffic_light}")
        traffic_light("SWITCH")
    

```
