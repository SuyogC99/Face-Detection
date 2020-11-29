import cv2

face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)
while True:
    _,img=cap.read()#you can also use ret,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 4)
    eyes = eye.detectMultiScale(gray,1.3,3)
    #for different colors to recognize eye and face
    for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    for (x, y, w, h) in eyes:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
    #for same colors to recognize eye and face
    '''lists=[faces,eyes]
    for i in range(len(lists)):
        for (x, y, w, h) in lists[i]:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)'''

    #Display
    cv2.imshow('img', img)
    k=cv2.waitKey(10)s
    #press ESC key to exit the webcam
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
    
