from itertools import count
import time
import pyautogui #Does not simulate via DirectX input, it uses virtual keys
import pydirectinput #DOES use DirectX input and not virtual keys.. worth clarifying
from inputs import get_gamepad
#from inputs import devices
from inputs import DeviceManager #access to device manager

minimum = -5000
maximum = 5000
positionVal = pyautogui.position() #get mouse position
position = [positionVal[0],positionVal[1]]
#for device in devices:
#   print(device)
#device = DeviceManager()  #DEvice manager is a list of all input devices,
print("Device Manager: ") # You could also input devices from inputs and it already does that
devices = DeviceManager()
for x in devices:
   print(x)
counter = 0
while True:
   events = get_gamepad()
   event = events[0]
   if event.ev_type == "Sync":
      continue
   #print(counter,"\n1:",event.ev_type,"\n2:", event.code,"\n3:", event.state)
   
   #ABSOLUTES
   if event.ev_type == "Absolute":
      match event.code:
      # LEFT JOYSTICK
         case "ABS_X": # X
            if event.state < minimum or event.state > maximum:
               position[0] += int(event.state/100)
               if position[0] < 0:
                  position[0] = 0
               elif position[0] > 1920:
                  position[0] -= position[0]-1920
               
               pydirectinput.moveTo(position[0],position[1],0.2) #try "move" not movetoo
               #print("ABS_X: ",event.state)
         case "ABS_Y": # Y (Is inverted, positive is down)
            if event.state < minimum or event.state > maximum:
               position[1] -= int(event.state/1000)
               if position[1] < 0:
                  position[1] = 0
               elif position[1] > 1080:
                  position[1] -= position[1]-1080
               pydirectinput.moveTo(position[0],position[1], 0.2)
               #print("ABS_Y: ",event.state)

      # RIGHT JOYSTICK
         case "ABS_RX": # X
            if event.state < minimum or event.state > maximum:
               print("ABS_RX: ",event.state)
         case "ABS_RY": # Y
            if event.state < minimum or event.state > maximum:
               print("ABS_RY: ",event.state)

         case "ABS_Z": #left trigger
            print("ABS_Z: ", event.state)
         case "ABS_RZ": #right trigger
            print("ABS_RZ: ", event.state)
         
         case "ABS_HAT0Y": # UP(-1) and DOWN(1) arrows
            print("ABS_HAT0Y: ",event.state)
         case "ABS_HAT0X": # LEFT(-1) and RIGHT(1) arrows
            print("ABS_HAT0X: ",event.state)

   #BUTTONS
   else: #event.ev_type == "Key":
      match event.code:
         case "BTN_SOUTH": #A button
            #print("BTN_SOUTH: ",event.state)
            if(event.state):
               pydirectinput.keyDown('a')
               print("a is down")
            else:
               pydirectinput.keyUp('a')
               print("a is up")
         case "BTN_EAST": #B button
            print("BTN_EAST: ",event.state)
            pydirectinput.click()
         case "BTN_NORTH": #Y button
            print("BTN_NORTH: ",event.state)
         case "BTN_WEST": #X button
            print("BTN_WEST: ",event.state)
         
         case "BTN_TL": #left button
            print("BTN_TL: ", event.state)
         case "BTN_TR": #right button
            print("BTN_TR: ", event.state)

         case "BTN_SELECT": #select button
            print("BTN_SELECT: ", event.state)
         case "BTN_START": #starts button
            print("BTN_START: ", event.state)
            quit()

         case "BTN_THUMBR": #right joystick click
            print("BTN_THUMBR: ", event.state)
         case "BTN_THUMBL": #left joystick click
            print("BTN_THUMBR: ", event.state)   

      
      #position = pyautogui.position()
      #pyautogui.moveTo((position[0]+int(event.state /1000)), (position[1]+int(event.state /1000)))
