# Bring in mss
from mss import mss
# Bring in opencv for rendering 
import cv2
import numpy as np
import time
# bring in pynput for round_predspress capture
from pynput.keyboard import Controller, Key 
import tensorflow as tf
import os
import matplotlib.pyplot as plt
import numpy as np
import pyautogui as pag
import keyboard as kb
import pydirectinput

Escape = True
currentkey = None
currentkey2 = None


class Capture(): 
    def __init__(self): 
        # Setup the game area 
        self.game_area = {"left": 100, "top": 425, "width": 850, "height":240}
        self.capture = mss()
        self.keys = []

        self.model = tf.keras.models.load_model('modeltype4.model')
        self.dark_green = (45, 25, 130)
        self.light_green = (85, 200, 222)
        self.dark_orange = (0, 25, 130)
        self.light_orange = (15, 255, 222)
        


    def make_move(self, currentkey, currentkey2):
        
        keyboard = Controller()

        print(f"CURRENT KEY IS {currentkey}")
        if kb.is_pressed("esc"):
            global Escape
            Escape = False
       
        gamecap = np.array(self.capture.grab(self.game_area))
        img = cv2.cvtColor(gamecap, cv2.COLOR_BGR2RGB)
        hsv_racing = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv_racing, self.dark_green, self.light_green)
        mask2 = cv2.inRange(hsv_racing, self.dark_orange, self.light_orange)
        finalmask = mask+mask2
        final_result = cv2.bitwise_and(img, img, mask=finalmask)
        final_result = cv2.cvtColor(final_result, cv2.COLOR_BGR2RGB)

        prediction = self.model.predict(tf.convert_to_tensor([final_result]))
        try:
            prediction[0][1] = prediction[0][1] * 0.75
        except:
            pass
        round_preds = np.around(prediction)
        print(round_preds)

        if np.all(round_preds == [[1., 0., 0., 0.]]):
            key = 'up'
            key2 = None
            print("UP ASSIGNED")
        if np.all(round_preds == [[0., 1., 0., 0.]]):
            key = 'down'
            key2 = None
            print("DOWN ASSIGNED")
        if np.all(round_preds == [[0., 0., 1., 0.]]):
            key = 'left'
            key2 = None
            print("LEFT ASSIGNED")
        if np.all(round_preds == [[0., 0., 0., 1.]]):
            key = 'right'
            key2 = None
            print("RIGHT ASSIGNED")
        if np.all(round_preds == [[1., 0., 1., 0.]]):
            key = 'left'
            key2 = 'up'
        if np.all(round_preds == [[0., 1., 1., 0.]]):
            key = 'left'
            key2 = 'down'
        if np.all(round_preds == [[1., 0., 0., 1.]]):
            key = 'right'
            key2 = 'up'
        if np.all(round_preds == [[0., 1., 0., 1.]]):
            key = 'right'
            key2 = 'down'
        if np.all(round_preds == [[0., 0., 0., 0.]]):
            key = None
            key2 = None

        if currentkey != None and (currentkey!=key or currentkey!=key2):
            pydirectinput.keyUp(currentkey)
        if currentkey2 != None and (currentkey2!=key or currentkey2!=key2):
            pydirectinput.keyUp(currentkey2)


        #if key == currentkey or key == currentkey2:
        #    pass
        #else:
        if key != None:
            pydirectinput.keyDown(key)
            print("key pressed")
        #if key2 == currentkey or key2 == currentkey2:
        #    pass
        #else:
        if key2 != None:
            pydirectinput.keyDown(key2)
            print("key pressed")
        
        return key, key2
if __name__ == '__main__':
    # Sleep for 10 seconds to allow us to get back into the game
    time.sleep(1)
    capture = Capture()
    while Escape:
        currentkey, currentkey2 = capture.make_move(currentkey, currentkey2)