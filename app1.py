import cv2
# print("package imported")
# img = cv2.imread("assets/myimage.jpg")
# grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(img,(7,7),0)
# imgCanny = cv2.Canny(img,100,100)
# cv2.imshow("Output",img)
# cv2.imshow("Output2",imgBlur)
# cv2.imshow("output3",grayimg)
# cv2.imshow("output4",imgCanny)
#
# cv2.waitKey(0)

#code for webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break