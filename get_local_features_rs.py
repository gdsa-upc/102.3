# -*- coding: utf-8 -*-
#self.extractor = cv2.DescriptorExtractor_create("SIFT")

from Parametres import parametres
from rootsift import RootSIFT
import cv2
#from matplotlib import pyplot as plt

def get_local_features_rs(imatge_entrada):
    params = parametres();#agafa els parametres de l'ordinador
    img = cv2.imread('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images',imatge_entrada]),0) # el 0 ho passa a nivells de gris
    #arreglo provisional
    #if img is None:
        #img=cv2.imread('/'.join([params['arrel_entrada'],params['bd_imatges'],params['val'],'images',imatge_entrada]),0)
    #fi arreglo provisional
# nombre màxim de kp a extreure
    #n=1000
    img = imatge_entrada
    #kp = orb.detect(img,None)  +  kp, des = orb.compute(img, kp)
    r = 400.0 / img.shape[1]
    print r
    dim = (400, int(img.shape[0] * r))
    rimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
# Iniciem el detector ORB
    rs = RootSIFT()
    detector = cv2.FeatureDetector_create(params['keypoint_type'])
    kps = detector.detect(img,None)
    kps, descs = rs.compute(img,kps)
    
    print "RootSIFT: kps=%d, descriptors=%s " % (len(kps), descs.shape)
    
    kps , descs= rs.compute(rimg,None)
    print descs

# dibuixa els descriptors sobre la imatge amb representació segons la importància
    #img_kp = cv2.drawKeypoints(img,kp,flags=4)
    #plt.imshow(img_kp),plt.show()

    return kps, descs;
