from captureScreen_mss import capture_screen, capture_screen_frames, capture_screen_region
from keystroke import press_key, hold_key
import time

if __name__ == "__main__":

    # gen = capture_screen_frames(2)

    # for frame in gen:
    #     pass
    # hold_key('up')
    monitor_num = 2  
    capture_screen_region(monitor_num)
