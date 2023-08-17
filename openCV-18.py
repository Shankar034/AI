import cv2
import numpy as np

x= np.zeros([256,560,3], dtype=np.uint8)
for rows in range(0,256,1):
    for column in range(0,560,1):
        x[rows,column]=(int(column/2), rows,255)

x= cv2.cvtColor(x,cv2.COLOR_HSV2BGR)

y= np.zeros([256,560,3], dtype=np.uint8)
for rows in range(0,256,1):
    for column in range(0,560,1):
        y[rows,column]=(int(column/2), 255,255)

y= cv2.cvtColor(y,cv2.COLOR_HSV2BGR)
while True:
    cv2.imshow("Frame",x)
    cv2.moveWindow("Frame",10,10)

    cv2.imshow("FrameY",y)
    cv2.moveWindow("FrameY",10,rows +40)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()