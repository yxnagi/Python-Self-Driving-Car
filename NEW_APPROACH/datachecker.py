import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

train_data = np.load('C:/Users/ayman/Documents/GitHub/COURSEWORK/NEW_APPROACH/training_data-1.npy', allow_pickle=True)

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test', img)
    print(choice)
    if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break