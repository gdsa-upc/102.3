# -*- coding: utf-8 -*-
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from itertools import islice
import numpy as np
from collections import defaultdict
from Parametres import parametres
import matplotlib.pyplot as plt
import collections


def plot_confusion_matrix(cm, true_labels,normalize = False,title='Confusion matrix', cmap=plt.cm.Blues):
    
    # Normalize matrix rows to sum 1
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    plt.imshow(cm, interpolation='nearest',cmap=cmap)
    
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(true_labels))
    plt.xticks(tick_marks, true_labels, rotation=90)
    plt.yticks(tick_marks, true_labels)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    plt.show()

def evaluate_classification():
    params = parametres()
    f=open((params['arrel_entrada']+'/'+params['bd_imatges']+'/val/annotation.txt'),'r') #obrim el fitxer ground truth de validació i llegim l'interior
    next(f)
    gt=[] #crea una llista amb la ground truth de validacio
    for line in f:
        a=line.index('\t')
        gt.append(line[a+1:])
    f.close()      
    f=open((params['arrel_sortida']+'/classification.txt'),'r') #fem el mateix amb el resultat de classify
    aa=[] #crea una llista amb el resultat
    for line in f:
        a=line.index('\t')
        aa.append(line[a+1:])
    f.close()
    #Acuracy
    print "Accuracy of system:" 
    print accuracy_score(gt,aa)
    print'\n'
   
    print "Precision:" 
    print precision_score(gt,aa,average='macro')
    print '\n'
    print "Recall:"
    print recall_score(gt,aa,average='macro')
    print '\n'
    print "f1_Score:" 
    print f1_score(gt,aa,average='macro')

    #Confusion matrix
    cm = confusion_matrix(gt,aa)
    classes = np.unique(gt) #llista de les classes
    plt.figure(1)
    plot_confusion_matrix(cm,classes,normalize=False)
    plt.figure(2)
    plot_confusion_matrix(cm,classes,normalize=True)