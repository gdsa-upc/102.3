import numpy as np
from sklearn import preprocessing
def build_bow(code):
    v=np.bincount(code)
    print v
    vn=preprocessing.normalize(v)
    return vn