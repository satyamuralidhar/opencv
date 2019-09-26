pip install opencv-python

pip install opencv-contrib-python

import cv2
import numpy as np
import matplotlib.pyplot as plt

!wget "https://raw.githubusercontent.com/satyamuralidhar/opencv/master/images/tiger.jpg"

img = cv2.imread('tiger.jpg')

import cv2
img = cv2.imread('tiger.jpg')
ret,thresh1 = cv2.threshold(img , 100 , 255 , cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img , 100 , 255 , cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img , 100 , 255 , cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img , 100 , 255 , cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img , 100 , 255 , cv2.THRESH_TOZERO_INV)

titles = ['oringinal' , 'binary' ,'binary_inv' ,'trunc' ,'tozero' ,'tozero_inv']
images = [img , thresh1 , thresh2 , thresh3 , thresh4 , thresh5]
for i in range(6):
    plt.subplot(2 3,i+1)
    plt.imshow(images[i] ,'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


