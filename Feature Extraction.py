# -*- coding: utf-8 -*-
from get_local_features_orb import get_local_features_orb
#from get_local_features_shift import get_local_features_shift
from Parametres import parametres
import numpy as np
import pickle

def Feature_extraction():
    
    #comença la inserció al diccionari
    images=open('Train_ID.txt', "r") #obre l'arxiu on hi ha les id's en mode lectura

    diccionari={} #crea un diccionari buit
    #per cada vegada que pugui llegir una línia (un id) del fitxer executa el loop sencer
    for img in images:
        i=img.rstrip('\n')
        #guarda a la posició 'img' del diccionari (una id que ha llegit) un vector que retorna la funcio que extreu característiques
        diccionari.update({i: get_local_features_orb(img)}) 
    images.close()
    with open('/diccionari.pickle', 'wb') as dic:
      pickle.dump(diccionari, dic)
    return;
    