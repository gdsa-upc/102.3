# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/Ariadna/Documents/audiovisuals 4t/GDSA/TerrassaBuildings900/train/images/38-29833-926.jpg',0)
# el 0 ho passa a nivells de gris
# Iniciem el detector ORB
orb = cv2.ORB()
# Detecta els punts clau a la imatge
kp = orb.detect(img,None)
# processa els descriptors amb l'ORB
kp, des = orb.compute(img, kp)
# dibuixa els descriptors sobre la imatge amb representació segons la importància
img2 = cv2.drawKeypoints(img,kp,flags=4)
plt.imshow(img2),plt.show()