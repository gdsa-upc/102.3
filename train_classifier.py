# -*- coding: utf-8 -*-
from sklearn import svm
import pickle
from Parametres import parametres

def train_classifier(dic_train,outdir,gtt):
    params = parametres()
    
    train_in = open(dic_train, 'rb')
    mydict = pickle.load(train_in)
    gtt_id = open(gtt, 'rb')
    gtt_dic = pickle.load(gtt_id)
    
    classes = []#inicialitzem el vector classes.
    for line in gtt_dic: #l'omplim només amb un valor/classe--després miraré com fer-ho amb el pes.
        classe = line[line.index("\t")+1:line.index("\n")]
        if classe not in classes:
            classes.append(line)
    
    #claus = mydict.keys()
    #BoW = mydict.values()
    
    valors = {} #diccionari classe:BoW
    for i in gtt_dic.keys(): #l'omplim amb els ids i classes de gtt i els bow de mydict
        for k in mydict.keys():
            if i == k:
                valors[i]= gtt_dic[k]
    print gtt_dic
                                  
    model = svm.SVC()   
    model.fit(valors, classes)
        
    #SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    #decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    #max_iter=-1, probability=False, random_state=None, shrinking=True,
    #tol=0.001, verbose=False) 
    
    with open(params['arrel_sortida']+'/model_classifier.pickle', 'wb') as save_model:
        pickle.dump(model,save_model)
    
    return