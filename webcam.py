import cv2

capture = cv2.VideoCapture(1)
 
while True:
    isTrue,pic = capture.read()
    cv2.imshow('frame',pic)
    if cv2.waitKey() & 0xFF==ord('q'):
        break
capture.release()
cv2.destroyAllWindows() 