from sklearn import preprocessing
def build_bow(code,nc):
    bow=[0]*nc
    for x in range(0,len(bow)):
        for i in code:
            if i==x:
                bow[x]+=1
    vn=preprocessing.normalize(bow)[0]
    return vn