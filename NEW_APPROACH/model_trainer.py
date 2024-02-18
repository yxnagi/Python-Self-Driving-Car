import numpy as np
from models import alexnet
import tflearn
import tensorflow as tf

WIDTH = 196
HEIGHT = 90
LR = 1e-3
EPOCH = 10

MODEL_NAME = "MODEL-{}-{}-{}-epochs.model".format(LR, "alexnet", EPOCH)

model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load('NEW_APPROACH/training_data-1.npy', allow_pickle=True)

train = train_data[: -1000]
test = train_data[-1000: ]

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
Y = [i[1] for i in train]

test_X = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
test_Y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCH,
          validation_set=({'input': test_X}, {'targets': test_Y}),
          snapshot_step=500, show_metric=True, run_id=MODEL_NAME,)

model.save(MODEL_NAME)