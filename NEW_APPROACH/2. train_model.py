import numpy as np
from grabscreen import grab_screen
import cv2
import time
import os
import pandas as pd
from tqdm import tqdm
from collections import deque
from models import alexnet as googlenet
from random import shuffle


FILE_I_END = 1860

WIDTH = 196
HEIGHT = 90
LR = 1e-3
EPOCHS = 30

MODEL_NAME = 'TRIAL_RUN1'
PREV_MODEL = ''

LOAD_MODEL = False

wl = 0
sl = 0
al = 0
dl = 0

wal = 0
wdl = 0
sal = 0
sdl = 0
nkl = 0

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

model = googlenet(WIDTH, HEIGHT, LRmodel_name=MODEL_NAME)

if LOAD_MODEL:
    model.load(PREV_MODEL)
    print('We have loaded a previous model!!!!')


try:
            file_name = 'NEW_APPROACH/training_data-1.npy'
            # full file info
            train_data = np.load(file_name, allow_pickle=True)
            print('training_data-1.npy',len(train_data))

            train = train_data[:-10000]
            test = train_data[-10000:]
            
            item_size = np.array(train[0][0]).size


            expected_size = WIDTH * HEIGHT * 1


            print("Individual Item Size:", item_size)
            print("Expected Size:", expected_size)



            X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
            Y = [i[1] for i in train]

            test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
            test_y = [i[1] for i in test]

            model.fit({'input': X}, {'targets': Y}, n_epoch=30, validation_set=({'input': test_x}, {'targets': test_y}), 
                snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)


            print('SAVING MODEL!')
            model.save(MODEL_NAME)
                    
except Exception as e:
            print(str(e))
            
    








#

#tensorboard --logdir=foo:J:/phase10-code/log

