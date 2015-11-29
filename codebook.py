import cv2
from scipy.cluster.vq import  whiten
import get_local_features
def codebook(ruta):
    keypoints, descriptores = get_local_features.get_local_features(ruta)
    whitened = whiten(descriptores)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1, 1.0) 
    ret,label,center= cv2.kmeans(whitened,4,criteria,1,cv2.KMEANS_PP_CENTERS)
    print(ret,label,center)