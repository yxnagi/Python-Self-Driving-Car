import pyautogui
from pynput.keyboard import Controller, Key 
import time


keyboard = Controller()
time.sleep(3)
print("hold")
keyboard.press(Key.up)
time.sleep(5)
keyboard.release(Key.up)