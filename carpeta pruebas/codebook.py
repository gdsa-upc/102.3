# -*- coding: utf-8 -*-
#import cv2
from sklearn.cluster import MiniBatchKMeans
from scipy.cluster.vq import  whiten,kmeans
def train_codebook(desc,nc):
    #whitened = whiten(desc[0:5])
    km = MiniBatchKMeans(nc)
    km.fit(desc)
    return km #kmeans(whitened, k)