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

def capture_screen_region(monitor_num):
    with mss.mss() as sct:
        while True:
            monitor = sct.monitors[monitor_num]
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            #define lane regions (using MS paint to approximate)
            left_lane = np.array([
                [725, 530],  #bl
                [850, 400],  #tl
                [925, 400],  #tr
                [875, 530]   #br
            ], dtype=np.int32)

            center_lane = np.array([
                [875, 530],
                [925, 400],
                [1000, 400],
                [1050, 530]
            ], dtype=np.int32)

            right_lane = np.array([
                [1050, 530],
                [1000, 400],
                [1075, 400],
                [1200, 530]
            ], dtype=np.int32)

            #draw regions
            cv2.polylines(frame, [left_lane], isClosed=True, color=(0, 0, 255), thickness=2)
            cv2.polylines(frame, [center_lane], isClosed=True, color=(0, 255, 0), thickness=2)
            cv2.polylines(frame, [right_lane], isClosed=True, color=(255, 0, 0), thickness=2)

            cv2.namedWindow("Second Monitor", cv2.WINDOW_NORMAL) #for window resizing
            cv2.imshow("Second Monitor", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
