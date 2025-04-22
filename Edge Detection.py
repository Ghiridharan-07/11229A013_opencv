import cv2
import numpy as np
image=cv2.imread(r"C:\Users\S.GHIRIDHARAN\PycharmProjects\PythonProject1\Bike.jpeg")
if image is None:
    print("Error:Could not open or find the image")
    exit()
blurred_image=cv2.GaussianBlur(image,(5,5),0)
edges=cv2.Canny(blurred_image,50,150)
cv2.imshow('orginal image',image)
cv2.imshow('Edge Detection',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()