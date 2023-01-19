# https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/
# https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html

import cv2
  
image = cv2.imread("images/redcup.jpg")

# converting BGR to RGB
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow('HSV',image_hsv)
cv2.imshow('RGB',image_rgb)
cv2.imshow('Gray',image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()