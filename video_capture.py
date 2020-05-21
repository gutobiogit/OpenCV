import numpy as np
import cv2

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while cap.isOpened:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_HLS2BGR_FULL )
    #gray2 = cv2.rectangle(gray,(0,0),(510,128),(0,255,0),5)
    #cv2.putText(gray2,'OpenCV',(10,300), font, 4,(255,255,255),2,cv2.LINE_AA)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()