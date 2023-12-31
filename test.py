# Bring in mss
from mss import mss
# Bring in opencv for rendering 
import cv2
import numpy as np
import time
import uuid
import os 
# bring in pynput for round_predspress capture
from pynput.keyboard import Controller, Key 
import tensorflow as tf
import os
import matplotlib.pyplot as plt
import numpy as np
import pyautogui as pag
import keyboard as kb

Escape = True
currentkey = None
currentkey2 = None


class Capture(): 
    def __init__(self): 
        # Setup the game area 
        self.game_area = {"left": 100, "top": 425, "width": 850, "height":240}
        self.capture = mss()
        self.keys = []

        self.model = tf.keras.models.load_model('modeltype3.model')


    def make_move(self):
        dark_green = (45, 25, 130)
        light_green = (85, 200, 222)
        dark_orange = (0, 25, 130)
        light_orange = (15, 255, 222)

        
        keyboard = Controller()

        print(f"CURRENT KEY IS {currentkey}")
        if kb.is_pressed("esc"):
            global Escape
            Escape = False
       
        gamecap = np.array(self.capture.grab(self.game_area))
        img = cv2.cvtColor(gamecap, cv2.COLOR_BGR2RGB)
        hsv_racing = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv_racing, dark_green, light_green)
        mask2 = cv2.inRange(hsv_racing, dark_orange, light_orange)
        finalmask = mask+mask2
        final_result = cv2.bitwise_and(img, img, mask=finalmask)
        final_result = cv2.cvtColor(final_result, cv2.COLOR_BGR2RGB)

        cv2.imshow("img", final_result)
        cv2.waitKey(0) 
        print("image shown")
        
if __name__ == '__main__':
    # Sleep for 10 seconds to allow us to get back into the game
    time.sleep(0.1)
    capture = Capture()
    capture.make_move()