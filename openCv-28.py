import os
import cv2
import face_recognition as FR
import pickle

encoding=[]
names= []

imageDir = 'C:\\Users\Dell\Documents\Python\demoimages\known'

for root, dirs,files in os.walk(imageDir):
    print(dirs)
    print(files)
    for file in files:
        print(file)