
from mss import mss
import cv2
import uuid
import numpy as np
import os

game_area = {"left": 0, "top": 30, "width": 1030, "height": 730}
capture = mss()

gamecap = np.array(capture.grab(game_area))
filename = (str(uuid.uuid1()))
cv2.imwrite(f'{filename}.png', gamecap)