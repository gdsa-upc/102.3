from sklearn import preprocessing
def build_bow(code,nc):
    bow=[0]*nc
    for x in range(0,len(bow)):
        for i in code:
            if i==x:
<<<<<<< HEAD
                bow[x]+=1
=======
                bow[x]=bow[x]+1
>>>>>>> refs/remotes/origin/master
    vn=preprocessing.normalize(bow)[0]
    return vn