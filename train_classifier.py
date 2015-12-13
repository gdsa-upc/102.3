# -*- coding: utf-8 -*-
from sklearn import svm
import pickle
from Parametres import parametres

def train_classifier():
    params = parametres()
    
    train_in = open(params['arrel_sortida']+'/dictrain.pickle','rb')
    mydict = pickle.load(train_in)
    f=open((params['arrel_entrada']+'/'+params['bd_imatges']+'/train/annotation.txt'),'r') #obrim el fitxer ground truth del train i llegim l'interior
    next(f)
    gtt_dic={} #crea un diccionari amb la ground truth de train
    for line in f:
        a=line.index('\t')
        gtt_dic[line[0:a]]=line[a+1:len(line)-1]
    f.close()
    
    #classes = []#inicialitzem el vector classes.
    #for classe in gtt_dic.values(): #l'omplim només amb un valor/classe--després miraré com fer-ho amb el pes.
    #    if classe not in classes:
    #        classes.append(classe)
    
    #BoW = mydict.values()
    
    valors = [] #creació de la llista on guardarem (en el mateix ordre) a quin edifici pertany cada BoW
    for i in gtt_dic.keys(): #recorrent el vector groundtruth
        for k in mydict.keys():
            if i == k:
                valors.append(gtt_dic[k]) #assignem a mida que trobem coincidencies el nom de l'edifici al final de la llista
    
    #El resultat ve a ser:
    #mydict.values()=[BoW1],[BoW2],...,[BoW450]
    #valors= edifici1,edifici2,...,edifici450
    #i queden lligats per l'ordre
                      
    model = svm.SVC()  
    model.fit(mydict.values(),valors)
        
    #SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    #decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    #max_iter=-1, probability=False, random_state=None, shrinking=True,
    #tol=0.001, verbose=False) 
    
    
    with open(params['arrel_sortida']+'/model_classifier.pickle', 'wb') as save_model:
        pickle.dump(model,save_model)
    
    return