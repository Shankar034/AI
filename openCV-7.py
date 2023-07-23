import cv2
import numpy as np
print(cv2.__version__)

boardSize =int (input("Hey Boss Enter the boardSize "))
numSquares = int(input("And also enter the numSquares ..."))
squareSize = int(boardSize/numSquares)

darkColor =(0,0,0)
whiteColor = (0,0,255)
nowColor = darkColor
while True:
    x= np.zeros([boardSize,boardSize,3],dtype=np.uint8)
    for rows in range(0,numSquares):
        for columns in range(0,numSquares):
            x[squareSize*rows:squareSize*(rows +1),squareSize*columns:squareSize*(columns+1)]=nowColor
            if nowColor==darkColor:
                nowColor=whiteColor
            else:
                nowColor=darkColor
    cv2.imshow('Webcam',x)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break


