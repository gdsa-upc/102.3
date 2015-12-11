# -*- coding: utf-8 -*-
from Parametres import parametres
import collections
import pickle
from scipy.spatial import distance


def rank():
    
    params=parametres()#parametres
    
    ft_in = open(params['arrel_sortida']+'/dictrain.pickle','rb')#abrimos el fichero pickle de entrenamiento
    train =pickle.load(ft_in)
    fq_in = open(params['arrel_sortida']+'/dicval.pickle','rb')#abrimos el fichero pickle del query
    val = pickle.load(fq_in)
    
    
    for i in val.keys():#The method keys() retorna una llista de totes les claus disponibles al diccionari
        output = open(params['arrel_sortida']+'/rankings/'+i+'.txt','w')#ficheros de salida 
        ranking={}
        for j in train.keys():
            ###
            dist=distance.euclidean(val[i], train[j])
            ranking[dist]=j
            ###
        rank_ord = collections.OrderedDict(sorted(ranking.items()))
        for k in rank_ord.values():
            output.write(k+'\n')
        output.close()
    ft_in.close()
    fq_in.close()