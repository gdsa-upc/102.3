from numpy import array
from scipy.cluster.vq import vq
from scipy.cluster.vq import whiten
def get_assignments(desc, codebook):
    d=whiten(desc)
    #code,dist=vq(d,codebook)
    code=codebook.predict(d)
    return code