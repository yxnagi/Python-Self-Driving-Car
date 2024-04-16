import numpy as np
import time
from pynput.keyboard import Controller, Key 
import keyboard as kb
import pyautogui
import pydirectinput

Escape = True
currentkey = None
currentkey2 = None


class Capture(): 
    def __init__(self): 
        self.keys = []

    def make_move(self, currentkey):

        time.sleep(1)
        
        round_preds = [[1., 0., 0., 0.]]

        print(f"CURRENT KEY IS {currentkey}")
        if kb.is_pressed("esc"):
            global Escape
            Escape = False
       
        if np.all(round_preds == [[1., 0., 0., 0.]]):
            key = 'up'
            print("UP ASSIGNED")
        if np.all(round_preds == [[0., 1., 0., 0.]]):
            key = 'down'
            print("DOWN ASSIGNED")
        if np.all(round_preds == [[0., 0., 1., 0.]]):
            key = 'left'
            print("LEFT ASSIGNED")
        if np.all(round_preds == [[0., 0., 0., 1.]]):
            key = 'right'
            print("RIGHT ASSIGNED")

        if currentkey != None and (currentkey!=key ):
            pydirectinput.keyUp(currentkey)
            print("key released")
        
        if key != None:
            pydirectinput.keyDown(key)
            print("key pressed1")

        return key
    
if __name__ == '__main__':
    for x in range(0,3,-1):
        print(x)
        time.sleep(1)
    capture = Capture()
    while Escape:
        currentkey = capture.make_move(currentkey)