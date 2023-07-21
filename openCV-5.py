import cv2

width = 480
height =360

rows = int(input("Boss, Enter the number of rows ?"))
columns= int (input("And also enter the number of columns"))

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(* 'MJPG'))

while True:
    ignore, frame = cam.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.resize(frame,(int(width/columns),int(height/columns)))
    for i in range(0,rows):
        for j in range(0,columns):
            frameName = " Wbecam "+str(i)+" x "+str(j)
            cv2.imshow(frameName,frame)
            cv2.moveWindow(frameName,(int(width/columns)*j),(int(height/columns +30)*i))

    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()