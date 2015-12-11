<<<<<<< HEAD

=======
>>>>>>> refs/remotes/origin/master
from sklearn.cluster import KMeans, MiniBatchKMeans
def train_codebook(desc,k):
    km= MiniBatchKMeans(k)
    km.fit(desc)
<<<<<<< HEAD
    return km 
=======
    return km
>>>>>>> refs/remotes/origin/master
