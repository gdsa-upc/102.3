# -*- coding: utf-8 -*-
from codebook import train_codebook
import pickle
from Parametres import parametres
from assignment import get_assignments
from get_local_features_orb import get_local_features_orb
from create_bow import build_bow
#from get_local_features_sift import get_local_features_sift
import numpy as np
import os 
import warnings
import matplotlib.pyplot as plt
from rank import rank
from evaluate_ranking import evaluate_ranking
warnings.filterwarnings("ignore")
def grafica_clusters():
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
    k=[100,500,1000,1500,2000]
    code_book1=train_codebook(descriptors,k[0])
    code_book2=train_codebook(descriptors,k[1])
    code_book3=train_codebook(descriptors,k[2])
    code_book4=train_codebook(descriptors,k[3])
    code_book5=train_codebook(descriptors,k[4])
    maps=[]
    
    #100 clusters
    ####Compute Assignaments
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    dic_train={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book1)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[0])
            img=img[0:-4]
            dic_train[img]=bow
        
    ###Construccion diccionari val    
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'], params['val'],'images'])) #llegeix els fitxers de la carpeta de validació
    dic_val={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book1)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[0])
            img=img[0:-4]
            dic_val[img]=bow
    with open(params['arrel_sortida']+'/dictrain.pickle', 'wb') as save_train:
        pickle.dump(dic_train,save_train)
    with open(params['arrel_sortida']+'/dicval.pickle', 'wb') as save_val:
        pickle.dump(dic_val,save_val)
    rank()
    map1=evaluate_ranking()
    maps.append(map1)
    
    #500 clusters
    ####Compute Assignaments
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    dic_train={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book2)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[1])
            img=img[0:-4]
            dic_train[img]=bow
        
    ###Construccion diccionari val    
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'], params['val'],'images'])) #llegeix els fitxers de la carpeta de validació
    dic_val={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book2)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[1])
            img=img[0:-4]
            dic_val[img]=bow
    with open(params['arrel_sortida']+'/dictrain.pickle', 'wb') as save_train:
        pickle.dump(dic_train,save_train)
    with open(params['arrel_sortida']+'/dicval.pickle', 'wb') as save_val:
        pickle.dump(dic_val,save_val)
    rank()
    map2=evaluate_ranking()
    maps.append(map2)
    
    #1500 clusters
    ####Compute Assignaments
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    dic_train={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book3)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[3])
            img=img[0:-4]
            dic_train[img]=bow
        
    ###Construccion diccionari val    
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'], params['val'],'images'])) #llegeix els fitxers de la carpeta de validació
    dic_val={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book4)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[3])
            img=img[0:-4]
            dic_val[img]=bow
    with open(params['arrel_sortida']+'/dictrain.pickle', 'wb') as save_train:
        pickle.dump(dic_train,save_train)
    with open(params['arrel_sortida']+'/dicval.pickle', 'wb') as save_val:
        pickle.dump(dic_val,save_val)
    rank()
    map3=evaluate_ranking()
    maps.append(map3)
    
    #1000 clusters
    ####Compute Assignaments
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    dic_train={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book4)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[3])
            img=img[0:-4]
            dic_train[img]=bow
        
    ###Construccion diccionari val    
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'], params['val'],'images'])) #llegeix els fitxers de la carpeta de validació
    dic_val={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book4)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[3])
            img=img[0:-4]
            dic_val[img]=bow
    with open(params['arrel_sortida']+'/dictrain.pickle', 'wb') as save_train:
        pickle.dump(dic_train,save_train)
    with open(params['arrel_sortida']+'/dicval.pickle', 'wb') as save_val:
        pickle.dump(dic_val,save_val)
    rank()
    map4=evaluate_ranking()
    maps.append(map4)

    #2000 clusters
    ####Compute Assignaments
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'],'train','images'])) #llegeix els fitxers de la carpeta d'entrenament
    dic_train={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book5)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[4])
            img=img[0:-4]
            dic_train[img]=bow
        
    ###Construccion diccionari val    
    images=os.listdir('/'.join([params['arrel_entrada'],params['bd_imatges'], params['val'],'images'])) #llegeix els fitxers de la carpeta de validació
    dic_val={}
    for img in images:
        if img!='Thumbs.db':
            kp_img, desc_img=get_local_features_orb(img)
            cl_img=get_assignments(desc_img,code_book5)
    
            ####Construct BoW vector
            bow=build_bow(cl_img, k[4])
            img=img[0:-4]
            dic_val[img]=bow
    with open(params['arrel_sortida']+'/dictrain.pickle', 'wb') as save_train:
        pickle.dump(dic_train,save_train)
    with open(params['arrel_sortida']+'/dicval.pickle', 'wb') as save_val:
        pickle.dump(dic_val,save_val)
    rank()
    map5=evaluate_ranking()
    maps.append(map5)

    #representació
    plt.plot(k,maps)
    plt.ylabel('Performance')
    plt.xlabel('Nr')
    
    plt.show()

    return