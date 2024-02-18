import pyautogui, time, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        CurserPos = pyautogui.position()
        print(CurserPos)
        sys.stdout.flush()
except:
    print("notworking")
    pass