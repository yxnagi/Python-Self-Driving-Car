import threading
import cv2
from getkeys import key_check
from directkeys import PressKey, ReleaseKey
from grabscreen import grab_screen
import numpy as np
import time
from models import alexnet

WIDTH = 196
HEIGHT = 90
LR = 1e-3
EPOCH = 10
keytime= 0.1

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

model = alexnet(WIDTH, HEIGHT, LR)
model.load("MODEL-0.001-alexnet-10-epochs.model")



for i in range (3, 0, -1):
    time.sleep(.5)
    print(i)

def press_key1(a, b, c, d):
    PressKey(a)
    ReleaseKey(b)
    ReleaseKey(c)
    ReleaseKey(d)
    time.sleep(keytime)

def press_key2(a, b, c, d):
    PressKey(a)
    PressKey(b)
    ReleaseKey(c)
    ReleaseKey(d)
    time.sleep(keytime)

def nokeys(a, b, c, d):
    ReleaseKey(a)
    ReleaseKey(b)
    ReleaseKey(c)
    ReleaseKey(d)
    time.sleep(keytime)

def Straight():
    thread_straight = threading.Thread(target=press_key1, args=(W, A, S, D))
    thread_straight.start()

def Right():
    thread_right = threading.Thread(target=press_key1, args=(D, W, S, A))
    thread_right.start()

def Left():
    thread_left = threading.Thread(target=press_key1, args=(A, W, S, D))
    thread_left.start()

def Brake():
    thread_brake = threading.Thread(target=press_key1, args=(S, A, W, D))
    thread_brake.start()

def StraightRight():
    thread_straightright = threading.Thread(target=press_key2, args=(W, D, S, A))
    thread_straightright.start()

def StraightLeft():
    thread_StraightLeft = threading.Thread(target=press_key2, args=(W, A, S, D))
    thread_StraightLeft.start()

def BrakeRight():
    thread_BrakeRight = threading.Thread(target=press_key2, args=(S, D, W, A))
    thread_BrakeRight.start()

def BrakeLeft():
    thread_BrakeLeft = threading.Thread(target=press_key2, args=(S, A, W, D))
    thread_BrakeLeft.start()

def Coast():
    thread_coast = threading.Thread(target=nokeys, args=(S, A, W, D))
    thread_coast.start()

def drive(idx):
    if idx == 0:
        Straight()
    elif idx == 1:
        Brake()
    elif idx == 2:
        Left()
    elif idx == 3:
        Right()
    elif idx == 4:
        StraightLeft()
    elif idx == 5: 
        StraightRight()
    elif idx == 6: 
        BrakeLeft()
    elif idx == 7:
        BrakeRight()
    elif idx == 8:
        Coast()

def main():
    paused = False
    while True:
        if not paused:
            ti = time.time()
            screen = grab_screen(region=(640,300,1280,780))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (WIDTH, HEIGHT))
            prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
            prediction[1] = prediction[1]*0.9
            idx = np.argmax(prediction)
            drive(idx)
            print( f"FPS: ( {time.time() - ti} ) ")
            print(f"prediction: ({prediction})")


        
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)


main()

