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

from BaseDataCollection import DataCollectionBase

Escape = True

class GamePlay(DataCollectionBase):
    def __init__(self, left, top, width, height, datalocation):
        super().__init__(left, top, width, height, datalocation)

        self.__dark_green = (45, 25, 130)
        self.__light_green = (85, 200, 222)
        self.__dark_orange = (0, 25, 130)
        self.__light_orange = (15, 255, 222)
        


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
        #appends keys to file
        print(current_keys)

        filename = os.path.join(self.__datalocation, str(uuid.uuid1()))
        gamecap = np.array(self.capture.grab(self.__game_area))
        cv2.imwrite(f'{filename}.png', gamecap)
        picture = cv2.imread(f"{filename}.png")
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        hsv_racing = cv2.cvtColor(picture, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv_racing, self.__dark_green, self.__light_green)
        mask2 = cv2.inRange(hsv_racing, self.__dark_orange, self.__light_orange)
        finalmask = mask+mask2
        final_result = cv2.bitwise_and(picture, picture, mask=finalmask)

        final_result = cv2.cvtColor(final_result, cv2.COLOR_BGR2RGB)
        cv2.imwrite(f'{filename}.png', final_result)
        np.savetxt(f'{filename}.txt', np.array([",".join(current_keys)]), fmt='%s')



if __name__ == '__main__':
    # Sleep for 10 seconds to allow us to get back into the game
    time.sleep(2)
    game = GamePlay(100, 425, 850, 240, "data3")
    while Escape:
        game.collect_gameplay()    # DRY AFTERNOON AND MEXICO