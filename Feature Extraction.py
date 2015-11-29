# -*- coding: utf-8 -*-
from train_codebook import train_codebook
from get_assignments import get_assignments
from get_local_features_orb import get_local_features_orb
from build_bow import build_bow
#from get_local_features_shift import get_local_features_shift
from Parametres import parametres
import numpy as np

def Feature_extraction(id_imatge):
    ####Extract Local Features
    images=open('Train_ID.txt', "r") #obre l'arxiu on hi ha les id's en mode lectura
    
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
    kp_img, desc_img=get_local_features_orb(id_imatge)
    cluster_pertanyent, dist_centrecluster_proper=get_assignments(desc_img,code_book)
    
    ####Construct BoW vector
    bow=build_bow(cluster_pertanyent, clusters)
    
    return bow
    