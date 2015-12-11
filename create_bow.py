from sklearn import preprocessing
import numpy as np
import math
def build_bow(code,nc):
    bow=np.zeros(nc)
    for x in range(0,len(bow)):
        for i in code:
            if i==x:
                bow[x]=bow[x]+1
    vn=preprocessing.normalize(bow)[0]
    return vn