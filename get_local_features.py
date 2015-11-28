# -*- coding: utf-8 -*-
import cv2
import resize_image
def get_local_features(ruta):
    img = cv2.imread(ruta) # Leemos la imagen que pasamos como parámetro
    rimg = resize_image(img)
    sift = cv2.SIFT() # calcula la lista de descriptores de la imagen
    keypoints, descriptores = sift.detectAndCompute(rimg,None) # obtinc els key points amb els seus descriptors
    #cambiar rimg por image cuando queramos hacerl ocon las imagenes completas
    return keypoints,descriptores

    