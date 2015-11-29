import cv2
from scipy.cluster.vq import  whiten
def train_codebook(desc,k):
    whitened = whiten(desc)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1, 1.0) 
    a, b, c= cv2.kmeans(whitened,k)#,criteria,1,cv2.KMEANS_PP_CENTERS)
    print a
    print b
    print c
    return a,b,c