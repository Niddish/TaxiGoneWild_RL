import pyautogui
import time

def press_key(key):
    pyautogui.press(key)
    print("%s key hit" % key)

def hold_key(key):
    pyautogui.keyDown(key)
    print("%s key pressed" % key)
    time.sleep(20)
    pyautogui.keyUp(key)
    print("%s key released" % key)