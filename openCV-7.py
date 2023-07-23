import cv2
import numpy as np
print(cv2.__version__)

boardSize =int (input("Hey Boss Enter the boardSize "))
numSquares = int(input("And also enter the numSquares ..."))
squareSize = boardSize/numSquares

while True:
    x= np.zeros([boardSize,boardSize,3],dtype=np.uint8)
    cv2.imshow('Webcam',x)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break


