import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",(500,500))
cv2.createTrackbar("Hue Min","Trackbar",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbar",17,179,empty)
cv2.createTrackbar("Saturation Min","Trackbar",168,255,empty)
cv2.createTrackbar("Saturation Max","Trackbar",255,255,empty)
cv2.createTrackbar("Value Min","Trackbar",45,255,empty)
cv2.createTrackbar("Value Max","Trackbar",255,255,empty)




frameWidth = 640
frameHeight = 480


#Read Using the Webcam
cap = cv2.VideoCapture(0)
#set width and height of the video window
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150) #setting video brightness





while True:
    # img = cv2.imread("Resources/lambo.jpg")
    ret,img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbar")
    s_min = cv2.getTrackbarPos("Saturation Min","Trackbar")
    s_max = cv2.getTrackbarPos("Saturation Max","Trackbar")
    v_min = cv2.getTrackbarPos("Value Min","Trackbar")
    v_max = cv2.getTrackbarPos("Value Max","Trackbar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("Output",img)
    cv2.imshow("OutputHSV",imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)


    cv2.waitKey(1)

