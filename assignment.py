from numpy import array
from scipy.cluster.vq import vq
from scipy.cluster.vq import whiten
def get_assignments(desc, codebook):
    code=codebook.predict(desc)
    return code 
