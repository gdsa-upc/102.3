# -*- coding: utf-8 -*-
from codebook import train_codebook
from Parametres import parametres
from assignment import get_assignments
from get_local_features_orb import get_local_features_orb
from create_bow import build_bow
#from get_local_features_sift import get_local_features_sift
from build_database import build_database
import numpy as np
import os 

def Feature_extraction():
    ####Extract Local Features
    params=parametres()
    #build_database('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images']), '/'.join([params['arrel_sortida'],'llista_imgs']))
    #images=open('/'.join([params['arrel_sortida'],'llista_imgs','ID.txt']), "r") #obre l'arxiu on hi ha les id's en mode lectura
    images = os.listdir('/'.join([params['arrel_sortida'],'llista_imgs','ID.txt']))
    descriptors=[]
    #per cada vegada que pugui llegir una línia (un id) del fitxer executa el loop sencer
    for img in images:
        k, des=get_local_features_orb(img)
        descriptors.append(des) 
    #images.close()
    #print descriptors; es para en aquest punt i no agafa bé els valors assignant None, None, ...
    
    ####Train CodeBook
    clusters=4
    code_book, dist, centres=train_codebook(descriptors,clusters)
    
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
    build_database('/'.join([params['arrel_entrada'],params['bd_imatges'],'val','images']), '/'.join([params['arrel_sortida'],'llista_imgs']))
    images=open('/'.join([params['arrel_sortida'],'llista_imgs','ID.txt']), "r") #obre l'arxiu on hi ha les id's en mode lectura
    
    
    dic_val={}
    for img in images:
        kp_img, desc_img=get_local_features_orb(img)
        cluster_pertanyent, dist_centrecluster_proper=get_assignments(desc_img,code_book)
    
        ####Construct BoW vector
        bow=build_bow(cluster_pertanyent, clusters)
        dic_val[img]=bow
    
    return dic_train,dic_val
    