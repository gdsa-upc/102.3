# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
def get_local_features(ruta):
    img = cv2.imread(ruta) # Leemos la imagen que pasamos como parámetro
    r = 400.0 / img.shape[1] # El atributo shape retorna las dimensiones del array. Si el array es (m,n) i.shape[1] retorna n
    dim = (400, int(img.shape[0] * r)) # 
    rimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    plt.imshow(img),plt.show()
    plt.imshow(rimg),plt.show()
    sift = cv2.SIFT() # calcula la lista de descriptores de la imagen
    keypoints, descriptores = sift.detectAndCompute(rimg,None)
    return keypoints,descriptores

    