# -*- coding: utf-8 -*-
from Parametres import parametres
import cv2
#from matplotlib import pyplot as plt

def get_local_features_orb(imatge_entrada):
    params = parametres();#agafa els parametres de l'ordinador
    img = cv2.imread('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images',imatge_entrada]),0) # el 0 ho passa a nivells de gris
    #arreglo provisional
    if img is None:
        img=cv2.imread('/'.join([params['arrel_entrada'],params['bd_imatges'],params['val'],'images',imatge_entrada]),0)
    #fi arreglo provisional
# nombre màxim de kp a extreure
    n=1000
# Iniciem el detector ORB
    orb = cv2.ORB(nfeatures=n)
    
#kp = orb.detect(img,None)  +  kp, des = orb.compute(img, kp)
    r = 400.0 / img.shape[1]
    dim = (400, int(img.shape[0] * r))
    rimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    kp , des= orb.detectAndCompute(rimg,None)

# dibuixa els descriptors sobre la imatge amb representació segons la importància
    #img_kp = cv2.drawKeypoints(img,kp,flags=4)
    #plt.imshow(img_kp),plt.show()

    return kp, des;
