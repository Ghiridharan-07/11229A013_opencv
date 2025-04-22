import cv2

img = cv2.imread(r"C:\Users\S.GHIRIDHARAN\PycharmProjects\PythonProject1\Bike.jpeg")
cv2.imshow("Bike.jpg", img)
cv2.imwrite("Bike.png", img)
cv2.imwrite("Bike.tiff", img)
cv2.imshow("Bike.png", img)
cv2.imshow("Bike.tiff", img)
cv2.waitKey(0)