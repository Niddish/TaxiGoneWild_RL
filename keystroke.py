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

def reset_game():
    coords = [
        (920, 605),  #play again
        (610, 807),  #start
        (962, 892),  #confirm start
    ]
    for x, y in coords:
        time.sleep(.75) #delay to prevent accidentally not starting
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(.75) #delay to prevent accidentally not starting
