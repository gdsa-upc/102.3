from sklearn.cluster import KMeans, MiniBatchKMeans
def train_codebook(desc,k):
    km= MiniBatchKMeans(k)
    km.fit(desc)
    return km