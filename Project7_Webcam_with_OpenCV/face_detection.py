import cv2


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg", 1)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.05,
minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

#print(faces)
#print(type(faces))
resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[1]/3)))

cv2.imshow("img",resized)
cv2.waitKey(1000)
cv2.destroyAllWindows()



img2=cv2.imread("news.jpg", 1)

gray_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

faces2=face_cascade.detectMultiScale(gray_img2, 
scaleFactor=1.1,
minNeighbors=5)

for x,y,w,h in faces2:
    img2=cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),3)

#print(faces)
#print(type(faces))
resized2=cv2.resize(img2,(int(img2.shape[1]/3),int(img2.shape[1]/3)))

cv2.imshow("img2",resized2)
cv2.waitKey(10000)
cv2.destroyAllWindows()
