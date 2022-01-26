from wsgiref import validate
import cv2
import numpy as np
import demo
from pyzbar.pyzbar import decode

#img = cv2.imread('myQR.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

prev = ''

qr_data=[]

while True:
    success, img = cap.read()
    barcode = decode(img)
    if len(barcode) > 0:
        barcode = barcode[0]
        data = barcode.data
        if data==prev:
            continue
        prev = data
        #print(data)
        mydata = data.decode('utf-8')
        print(mydata)
        a=demo.validiate(mydata)
        print(a)

        qr_data.append(mydata)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2) 

    cv2.imshow('Result',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
print(qr_data)

cap.release()
cv2.destroyAllWindows()