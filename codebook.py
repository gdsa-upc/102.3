# -*- coding: utf-8 -*-
#import cv2
from scipy.cluster.vq import  whiten,kmeans
def train_codebook(desc,k):
    whitened = whiten(desc[0:5])
    #criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1, 1.0) 
    #a, b, c= cv2.kmeans(whitened,k,criteria,1,cv2.KMEANS_PP_CENTERS)
    #prints de comprovació, esborrar-los
    
    return kmeans(whitened, k)