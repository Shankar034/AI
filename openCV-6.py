import cv2
import numpy as np
print(cv2.__version__)

while True:
    frame=np.zeros([255,255], dtype= np.uint8)
    frame[:,:]=125
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break