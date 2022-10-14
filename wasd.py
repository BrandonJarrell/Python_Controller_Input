from curses import beep
import pydirectinput  ##DOES use DirectX input and not virtual keys.. worth clarifying
import time
from inputs import get_key, devices
print(devices.keyboards)

events = get_key()
event = events[0]
print(event.ev_type, event.code, event.state)