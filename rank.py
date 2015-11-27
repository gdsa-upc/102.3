# -*- coding: utf-8 -*-
import random
import pickle
def rank(query_features,train_features,outdir):
    ft_in = open(train_features,'rb')#abrimos el fichero pickle de entrenamiento
    train =pickle.load(ft_in)
    fq_in = open(query_features,'rb')#abrimos el fichero pickle del query
    rango = pickle.load(fq_in)
    for i in rango.keys():#The method keys() retorna una llista de totes les claus disponibles al diccionari
        output = open(outdir+'/'+i+'.txt','w')#ficheros de salida 
        for j in train.keys():
            f=random.choice(train.keys())
            output.write(f+'\n')#The method choice() retorna un element aleatòri d'una llista
        output.close()
    ft_in.close()
    fq_in.close()