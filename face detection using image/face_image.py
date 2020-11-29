import cv2

face_image=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('friends.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_image.detectMultiScale(gray,1.3,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
    
cv2.imshow('Face detected',img)

'''if the image is not fully showed on window then use imwrite command
to store then in file path you can see the image'''

cv2.imwrite('facedetected.jpg',img)

