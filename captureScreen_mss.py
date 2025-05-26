import mss
import numpy as np
import cv2

#captures screen and displays it in real-time (~30 FPS)
def capture_screen(monitor_num):
    with mss.mss() as sct:
        while True:
            monitor = sct.monitors[monitor_num]  
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            cv2.imshow("Second Monitor", frame)

            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

#captures frames for usage in RL/computer vision applications
def capture_screen_frames(monitor_num):
    framecount = 0
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_num]
        while True:
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            #check to see that frames are being captured correctly
            framecount += 1
            print("Number of frames = %d " % framecount)

            yield frame