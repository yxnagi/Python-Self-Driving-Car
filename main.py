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

Escape = True

class GamePlay(): 
    def __init__(self): 
        # Setup the game area 
        self.game_area = {"left": 100, "top": 425, "width": 850, "height":240}
        self.capture = mss()
        self.current_keys = []

    def collect_gameplay(self):
        
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

        filename = os.path.join('data2', str(uuid.uuid1()))
        gamecap = np.array(self.capture.grab(self.game_area))
        cv2.imwrite(f'{filename}.png', gamecap)
        np.savetxt(f'{filename}.txt', np.array([",".join(current_keys)]), fmt='%s')
        time.sleep(0.1)


if __name__ == '__main__':
    # Sleep for 10 seconds to allow us to get back into the game
    time.sleep(2)
    game = GamePlay()
    while Escape:
        game.collect_gameplay()    # DRY AFTERNOON AND MEXICO