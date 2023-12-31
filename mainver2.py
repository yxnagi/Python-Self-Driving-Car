# Bring in mss
from mss import mss
# Bring in opencv for rendering 
import cv2
import numpy as np
import time
import uuid
import os 
# bring in pynput for keypress capture
import keyboard


import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

from matplotlib.colors import hsv_to_rgb

import PIL.Image as Image

Escape = True

class GamePlay():
    
    def __init__(self): 
        # Setup the game area 
        self.game_area = {"left": 100, "top": 425, "width": 850, "height":240}
        self.capture = mss()
        self.current_keys = []
  

    def collect_gameplay(self):
        dark_green = (45, 25, 130)
        light_green = (85, 200, 222)
        dark_orange = (0, 25, 130)
        light_orange = (15, 255, 222)


        # Collect the frames
        rightpressed = False
        leftpressed = False 
        uppressed = False
        downpressed = False

        if keyboard.is_pressed("left arrow"):
            leftpressed = True
        if keyboard.is_pressed("right arrow"):
            rightpressed = True
        if keyboard.is_pressed("down arrow"):
            downpressed = True
        if keyboard.is_pressed("up arrow"):
            uppressed = True
        if keyboard.is_pressed("esc"):
            global Escape
            Escape = False
        current_keys = []
        if rightpressed:
            current_keys.append("right arrow")
        if leftpressed:
            current_keys.append("left arrow")
        if downpressed:
            current_keys.append("down arrow")
        if uppressed:
            current_keys.append("up arrow")
        print(current_keys)

        filename = os.path.join('data3', str(uuid.uuid1()))
        gamecap = np.array(self.capture.grab(self.game_area))
        cv2.imwrite(f'{filename}.png', gamecap)
        picture = cv2.imread(f"{filename}.png")
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        hsv_racing = cv2.cvtColor(picture, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv_racing, dark_green, light_green)
        mask2 = cv2.inRange(hsv_racing, dark_orange, light_orange)
        finalmask = mask+mask2
        final_result = cv2.bitwise_and(picture, picture, mask=finalmask)

        final_result = cv2.cvtColor(final_result, cv2.COLOR_BGR2RGB)
        cv2.imwrite(f'{filename}.png', final_result)
        np.savetxt(f'{filename}.txt', np.array([",".join(current_keys)]), fmt='%s')
        time.sleep(0.025)


if __name__ == '__main__':
    # Sleep for 10 seconds to allow us to get back into the game
    time.sleep(2)
    game = GamePlay()
    while Escape:
        game.collect_gameplay()    # DRY AFTERNOON AND MEXICO