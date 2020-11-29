import cv2
eye=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes=eye.detectMultiScale(gray,1.3,4)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display
    cv2.imshow('img', img)
    #press ESC key to exit the webcam
    k=cv2.waitKey(10)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
