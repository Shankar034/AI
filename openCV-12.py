import cv2

height= 680
width =460

snipW=140
snipH=90

boxCC=int(width/2)
boxRC=int(height/2)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    colorB=frame[int(boxRC-snipH/2):int(boxRC+snipH/2),int(boxCC-snipW/2):int(boxCC+snipW/2)]
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame= cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[int(boxRC-snipH/2):int(boxRC+snipH/2),int(boxCC-snipW/2):int(boxCC+snipW/2)]=colorB
    cv2.imshow("Frame2",colorB)
    cv2.moveWindow("Frame2",height,0)
    cv2.imshow("Frame1",frame)
    cv2.moveWindow("Frame1",0,0)
    
     
            
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release