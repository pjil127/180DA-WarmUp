# https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html

import numpy as np
import cv2
from matplotlib import pyplot as plt

webcam = cv2.VideoCapture(0)

ret, imageFrame = webcam.read()

while ret:
    ret, imageFrame = webcam.read()

    edges = cv2.Canny(imageFrame,100,200)
    plt.subplot(121),plt.imshow(imageFrame,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()