import time
import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector
#import sayacekranı.py

size = 200
a = cv2.imread("1.png")
a = cv2.resize(a, (size, size))
b = cv2.imread("2.png")
b = cv2.resize(b, (size, size))
c = cv2.imread("3.png")
c = cv2.resize(c, (size, size))
none=cv2.imread("none.png")
none = cv2.resize(none, (size, size))

detector= HandDetector(detectionCon=0.8,maxHands=1)
cap=cv2.VideoCapture(0)
hamle=None

while True:
    
    img2gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    img2gray1 = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    img2gray2 = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)
    img2gray3 = cv2.cvtColor(none, cv2.COLOR_BGR2GRAY)
    
    hands, mask = cv2.threshold(img2gray, 4, 255, cv2.THRESH_BINARY)
    hands, mask1 = cv2.threshold(img2gray1, 4, 255, cv2.THRESH_BINARY)
    hands, mask2 = cv2.threshold(img2gray2, 4, 255, cv2.THRESH_BINARY)
    hands, mask3 = cv2.threshold(img2gray3, 4, 255, cv2.THRESH_BINARY)
    
    success, img=cap.read()
    img = cv2.flip(img,1)
    hands, img=detector.findHands(img)
    img = cv2.resize(img, (0,0), fx=1.5, fy=1.5)
    #Ayna görüntüsü;
    def my_move():
        if hands:
            hand1=hands[0]
            lmlist1=hand1["lmList"]
            bbox1=hand1["bbox"]
            centerPoint1=hand1["center"]
            handType1=hand1["type"]
            fingers1=detector.fingersUp(hand1)
            parmaklar=fingers1[0]+fingers1[1]+fingers1[2]+fingers1[3]+fingers1[4]
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            if parmaklar==0:
                hamle="Taş"
                roi = img[30:size+30, 30:size+30]
                return "taş"
                roi[np.where(mask)] = 0
                roi += a
                
                
            elif parmaklar==2:
               hamle="Makas"
               
               roi2 = img[30:size+30, 30:size+30]
               return "makas"
               roi2[np.where(mask2)] = 0
               roi2 += c
               
            elif parmaklar==5 or parmaklar==4:
               hamle="Kağıt"
               roi1 = img[30:size+30, 30:size+30]
               return "kağıt"
               roi1[np.where(mask1)] = 0
               roi1 += b
               
            else:
                hamle="None"
                #time.sleep(2)
                return "none"
                roi3 = img[30:size+30, 30:size+30]
                roi3[np.where(mask3)] = 0
                roi3 += none
            my_move()
            
    #cv2.imshow("camera", img)    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


my_move()
cap.release()
cv2.destroyAllWindows()

# importing the libraries
