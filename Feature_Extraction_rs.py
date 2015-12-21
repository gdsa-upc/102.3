# -*- coding: utf-8 -*-
from codebook import train_codebook
import pickle
from Parametres import parametres
from assignment import get_assignments
from get_local_features_rs import get_local_features_rs
from create_bow import build_bow
#from get_local_features_sift import get_local_features_sift
import numpy as np
import os 
import warnings
warnings.filterwarnings("ignore")
def Feature_extraction():
    ####Extract Local Features
    params=parametres()
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    descriptors=[]
    for img in images:
        if img!='Thumbs.db':
            k, des=get_local_features_orb(img)
            if len(descriptors)==0:
                descriptors=des
            else:
                descriptors=np.vstack((descriptors,des))
    
    ####Train CodeBook
    clusters=4000
    code_book=train_codebook(descriptors,clusters)
    ####Compute Assignaments
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    dic_train={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_rs(img)
            cl_img=get_assignments(desc_img,code_book)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, clusters)
            img=img[0:-4]
            dic_train[img]=bow
        
    ###Construccion diccionari val    
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'], params['val'],'images'])) #llegeix els fitxers de la carpeta de validació
    dic_val={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, clusters)
            img=img[0:-4]
            dic_val[img]=bow
    with open(params['arrel_sortida']+'/dictrain.pickle', 'wb') as save_train:
        pickle.dump(dic_train,save_train)
    with open(params['arrel_sortida']+'/dicval.pickle', 'wb') as save_val:
        pickle.dump(dic_val,save_val)
    return
