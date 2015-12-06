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
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    descriptors=[]
    for img in images:
        k, des=get_local_features_orb(img)
        if des is not None:
            if len(descriptors)==0:
                descriptors=des
            else:
                descriptors=np.vstack((descriptors,des))
    
    ####Train CodeBook
    clusters=4
    code_book=train_codebook(descriptors,clusters)
    ####Compute Assignaments
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    dic_train={}
    for img in images:
        kp_img, desc_img=get_local_features_orb(img)
        if desc_img is not None:
            cl_img=get_assignments(desc_img,code_book)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, clusters)
            img=img[0:-4]
            dic_train[img]=bow
        
    ###Construccion diccionari val    
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'val','images'])) #llegeix els fitxers de la carpeta de validació
    dic_val={}
    for img in images:
        kp_img, desc_img=get_local_features_orb(img)
        if desc_img is not None:
            cl_img=get_assignments(desc_img,code_book)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, clusters)
            img=img[0:-4]
            dic_val[img]=bow
    print len(dic_val)
    print len(dic_train)
    return dic_train,dic_val
    