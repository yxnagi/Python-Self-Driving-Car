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

        filename = os.path.join('data2', str(uuid.uuid1()))
        gamecap = np.array(self.capture.grab(self.game_area))
        cv2.imwrite(f'{filename}.png', gamecap)
        time.sleep(0.1)


if __name__ == '__main__':
    # Sleep for 10 seconds to allow us to get back into the game
    time.sleep(2)
    game = GamePlay()
    while Escape:
        game.collect_gameplay()
        time.sleep(5)    # DRY AFTERNOON AND MEXICO