import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# print(cap)
while True:
   # Capture frame-by-frame
    ret, frame = cap.read()    
    #To change the color into gray
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)  
    #To quit the instance 
    #This code is necessary ,your app may not work without this code
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

        
cap.release()
cv2.destroyAllWindows()