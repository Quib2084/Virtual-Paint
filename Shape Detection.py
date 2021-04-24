import cv2
import numpy as np

def getContour(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objectType = "Triangle"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Sqaure"
                else:
                    objectType = "Rectangle"
            else:
                objectType = "None" 
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
path = "Resources/Shapes.jpg"
img = cv2.resize(cv2.imread(path),(720,720))

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgContour = img.copy()
getContour(imgCanny)

img_h = cv2.hconcat([imgGray,imgBlur,imgCanny])
# cv2.imshow("Stacked Output",img_h)
cv2.imshow("Output",imgContour)
cv2.waitKey(0)