import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Gerard/Pictures/a.jpg',0)
# el 0 ho passa a nivells de gris

# Iniciem el detector ORB
orb = cv2.ORB()

# Detecta els punts clau a la imatge
kp = orb.detect(img,None)

# compute the descriptors with ORB
#kp, des = orb.compute(img, kp)

img2 = cv2.drawKeypoints(img,kp,flags=4)
plt.imshow(img2),plt.show()

