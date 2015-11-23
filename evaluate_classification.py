# -*- coding: utf-8 -*-
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from itertools import islice
import numpy as np
from collections import defaultdict



#el codi no funciona i no llegeix bé dels fitxers txt d'entrada

def evaluate_classification(Aut_anot, grown_truth):
    f=open(Aut_anot, "r")
    lines=islice(f,1,None)
    
    #####línies 12-29: llegeix línia a línia i buscant el tabulafor agafa l'argument de cada ID (que és el que necessita)
    dic_gt=[] #crea una llista buida
    for line in lines:
        inici=line.index("\t")
        fi=len(line)
        dic_gt.append(line[inici:fi])
    f.close()

    f=open(Aut_anot, "r")
    lines=islice(f,1,None)
       
    dic_aa={} #crea una llista buida
    for line in lines:
        inici=line.index('\t')
        fi=len(line)
        dic_aa.append(line[inici:fi])  
    f.close()  
    #####
    
    #Acuracy
    Accuracy=accuracy_score(dic_gt, dic_aa)
    print "Accuracy of system: %d" %Accuracy

    Precision={}
    Recall={}
    f1_score={}
    #classification_report dóna: precision, recall, f1-score i support(que no el necessitem) per cada classe
    for i in range(13):
        classe, prec, rec, f1_s, _ =classification_report(dic_gt, dic_aa)
        Precision[classe]=prec
        print "Classe %d" %i
        print "Precision: %d: " %prec
        Recall[classe]=rec
        print "Recall: %d: " %rec
        f1_score[classe]=f1_s
        print "f1_Score: %d: " %f1_s
    
    #Average precision
    print "Average precision: "
    avg_pre=sum(p['value'] for p in Precision) / len(Precision)
    print avg_pre

    #Recall
    print "Recall: "
    Recalltot=len(Recall)/180
    print 
    
    #f1_score
    print "f1_score: "
    print (2*Recalltot*avg_pre)/(Recalltot+avg_pre)


    #Confusion matrix
    mc=confusion_matrix(dic_gt, dic_aa)
    print "Confusion Matrix: "
    print mc