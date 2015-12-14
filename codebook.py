from sklearn.cluster import MiniBatchKMeans
def train_codebook(desc,k):
    km= MiniBatchKMeans(k)
    km.fit(desc)
    return km