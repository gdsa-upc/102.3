# -*- coding: utf-8 -*-
from codebook import train_codebook
from assignment import get_assignments
from get_local_features_orb import get_local_features_orb
from create_bow import build_bow
#from get_local_features_shift import get_local_features_shift
from Parametres import parametres
from build_database import build_database
import numpy as np

def Feature_extraction():
    ####Extract Local Features
    build_database(path imatges train, path RdE)
    images=open('ID.txt', "r") #obre l'arxiu on hi ha les id's en mode lectura
    
    descriptors=[] 
    #per cada vegada que pugui llegir una línia (un id) del fitxer executa el loop sencer
    for img in images:
        k, des=get_local_features_orb(img)
        descriptors = np.concatenate((descriptors, des),axis=0) 
    images.close()
    
    ####Train CodeBook
    clusters=4
    code_book, dist, centres=train_codebook(clusters, descriptors)
    
    ####Compute Assignaments
    images=open('ID.txt', "r") #obre l'arxiu on hi ha les id's en mode lectura
    dic_train={}
    for img in images:
        kp_img, desc_img=get_local_features_orb(img)
        cluster_pertanyent, dist_centrecluster_proper=get_assignments(desc_img,code_book)
    
        ####Construct BoW vector
        bow=build_bow(cluster_pertanyent, clusters)
        dic_train[img]=bow
        
    ###Construccion diccionari val
    build_database(path imatges val, path RdE)
    #compute assignaments
    images=open('ID.txt', "r") #obre l'arxiu on hi ha les id's en mode lectura
    dic_val={}
    for img in images:
        kp_img, desc_img=get_local_features_orb(img)
        cluster_pertanyent, dist_centrecluster_proper=get_assignments(desc_img,code_book)
    
        ####Construct BoW vector
        bow=build_bow(cluster_pertanyent, clusters)
        dic_val[img]=bow
    
    return dic_train,dic_val
    