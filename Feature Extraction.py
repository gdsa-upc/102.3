# -*- coding: utf-8 -*-
import numpy as np
import pickle
def extraccio_caract(str):
    features=np.random.random_integers(0,100,(1,100))
    return features;
#def Feature_extraction(dir_imatges, IDs_file, dir_out):
def Feature_extraction(IDs_file, dir_out):
    #comença la inserció al diccionari
    images=open(IDs_file, "r") #obre l'arxiu on hi ha les id's en mode lectura

    diccionari={} #crea un diccionari buit
    #per cada vegada que pugui llegir una línia (un id) del fitxer executa el loop sencer
    for img in images:
        i=img.rstrip('\n')
        #guarda a la posició 'img' del diccionari (una id que ha llegit) un vector que retorna la funcio que extreu característiques
        diccionari.update({i: extraccio_caract(img)}) 
    images.close()
    with open(dir_out+'/diccionari.pickle', 'wb') as dic:
      pickle.dump(diccionari, dic)
    return;
    