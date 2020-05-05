from fsm import StateMachine, State
import time
traffic_light = StateMachine("LIGHT_GREEN")

light_green = State()
light_yellow = State()
light_red = State()

traffic_light["LIGHT_GREEN"] = light_green
traffic_light["LIGHT_YELLOW"] = light_yellow
traffic_light["LIGHT_RED"] = light_red

@light_green.transition
def switch():
    return "LIGHT_YELLOW"


@light_yellow.transition
def switch():
    return "LIGHT_RED"

@light_red.transition
def switch():
    return "LIGHT_GREEN"

if __name__ == "__main__":
    while True:
        print("Current State: " + traffic_light.state)
        time.sleep(7)
        traffic_light("SWITCH")
        print("Current State: " + traffic_light.state)
        time.sleep(4)
        traffic_light("SWITCH")
        print("Current State: " + traffic_light.state)
        time.sleep(7)
        traffic_light("SWITCH")
