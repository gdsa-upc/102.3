import random
import pickle
def rank(tipo,features_dir,train_features,outdir):
    train_in = open(train_features,'rb')#abrimos el fichero pickle de entrenamiento
    train =pickle.load(train_in)
    ftres_in = open(features_dir+tipo+'/_diccionari.pkl','rb')#abrimos el fichero pickle val o set
    rango = pickle.load(ftres_in)
    for i in rango.keys():#The method keys() returns a list of all the available keys in the dictionary.
        output = open(outdir+'/'+tipo+'_rank/'+i+'.txt','w')#ficheros de salida 
        for j in train.keys():
            output.write(random.choice(train.keys())+'\n')#The method choice() returns a random item from a list, tuple, or string.
        output.close()
    train_in.close()
    ftres_in.close()
        