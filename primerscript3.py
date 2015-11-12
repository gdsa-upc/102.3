import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Ariadna/Documents/audiovisuals 4t/GDSA/102.3/Castell_Cartoixa/castell_cartoixa_01.jpg',0)

# Initiate STAR detector
star = cv2.FeatureDetector_create("STAR")

# Initiate BRIEF extractor
#brief = cv2.DescriptorExtractor_create("BRIEF")

# find the keypoints with STAR
kp = star.detect(img,None)

# compute the descriptors with BRIEF
#kp, des = brief.compute(img, kp)

#print brief.getInt('bytes')
#print des.shape
img2=cv2.drawKeypoints(img,kp)
cv2.imshow('punts dinteres',img2)
