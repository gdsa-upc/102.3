# -*- coding: utf-8 -*-
from Parametres import parametres
import collections
import pickle
from scipy.spatial import distance


def rank(query_features,train_features):
    
    params=parametres()#parametres
    
    ft_in = open(train_features,'rb')#abrimos el fichero pickle de entrenamiento
    train =pickle.load(ft_in)
    fq_in = open(query_features,'rb')#abrimos el fichero pickle del query
    rango = pickle.load(fq_in)
    
    ranking={}
    
    for i in rango.keys():#The method keys() retorna una llista de totes les claus disponibles al diccionari
        output = open(params('arrel_sortida')+'/'+i+'.txt','w')#ficheros de salida 
        for j in train.keys():
            ###
            dist=distance.euclidean(i, j)
            ranking[dist]=i
            ###
        rank_ord = collections.OrderedDict(sorted(ranking.items()))
        output.write(rank_ord.values()+'\n')
        output.close()
    ft_in.close()
    fq_in.close()