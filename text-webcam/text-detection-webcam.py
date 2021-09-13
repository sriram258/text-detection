import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:

    _,img = cap.read()

    hImg, wImg,_ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        #print(b)
        b = b.split(' ')
        #print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
        cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,255,0),2)
    cv2.imshow("Result",img)
    cv2.waitKey(1)