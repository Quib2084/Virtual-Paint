#Project Virtual Paint

import cv2
import numpy as np

def findColor(img,myColors,myColorValues):
    count = 0
    newPoints = []
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array([color[0],color[2],color[4]])
        upper = np.array([color[1],color[3],color[5]])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContour(mask)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints

def getContour(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h =  0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 20, myColorValues[point[2]], cv2.FILLED)


 #################################################################################################

myColors = [
    [165, 179, 63, 153, 227, 255], #Red  h_min,h_max,s_min,s_max,v_min,v_max
    [52, 75, 62, 146, 172, 255],  #Green
    [109, 122, 62, 184, 229, 255] #purple
]

myColorValues = [
    [0,0,255],     #in BGR Format
    [0,255,0],
    [204,50,153]
]

myPoints = [] # [x, y, ColorId]

frameWidth = 1920
frameHeight = 1080

#Read Using the Webcam
cap = cv2.VideoCapture(0)
#set width and height of the video window
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150) #setting video brightness



while True:
    success, img = cap.read() #returns true if read successfully and the frame
    img = cv2.flip(img,1)
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)

    if len(newPoints)!=0:
        for point in newPoints:
            myPoints.append(point)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Result",imgResult);

    #cv2.waitkey(1) returns 32 bit int corresponding to the key pressed, mask that with 0xFF(11111111)
    #So this checks if button q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break