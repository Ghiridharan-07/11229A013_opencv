import cv2
img = cv2.imread(r"C:\Users\S.GHIRIDHARAN\PycharmProjects\PythonProject1\Bike.jpeg")
cv2.imshow("bike", img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)