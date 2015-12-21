# -*- coding: utf-8 -*-
import pickle
from Parametres import parametres
import numpy as np

# Functions to save solution files in the correct format for Kaggle Competition

def save_classification_file():
    params = parametres()
    '''
    Saves the classification results in the format:
    Id,Prediction
    24551-2934-8931,ajuntament
    30017-26696-17117,desconegut
    3398-20429-27862,farmacia_albinyana
    4611-17202-4774,catedral
    etc
    :param file_to_save: name of the file to be saved
    :param names: list of image ids
    :param labels: list of predictions to the image Ids
    '''
    file_to_save = open(params['arrel_sortida']+'/rankings/'+'kaggle_classification'+'.csv','w')
    f=open((params['arrel_entrada']+'/'+params['bd_imatges']+'/'+params['val']+'/annotation.txt'),'r') #obrim el fitxer ground truth de validació i llegim l'interior
    next(f)
    names=[]
    labels=[]
    for line in f:
        a=line.index('\t')
        names.append(line[0:a])
        labels.append(line[a+1:])
    f.close()    
    
    # Write header
    file_to_save.write("Id,Prediction\n")

    # Write image Ids and class labels
    for i in range(len(names)):
        file_to_save.write(names[i] + ','+ labels[i] + '\n')

    file_to_save.close()


def save_ranking_file(file_name,image_id,ranking):
    params = parametres()
    '''
    :param file_to_save: name of the file to be saved
    :param image_id: name of the query image
    :param ranking: ranking for the image image_id
    :return: the updated state of the file to be saved
    '''
    file_to_save = open(params['arrel_sortida']+'/rankings/'+file_name+'.txt','w')
    # Write query name
    file_to_save.write(image_id.split('.')[0] + ',')

    # Convert elements to string and ranking to list
    ranking = np.array(ranking).astype('str').tolist()
    
    # Write space separated ranking
    for item in ranking:
        file_to_save.write(item[0] + " ")

    file_to_save.write('\n')

    return file_to_save

def crea_rankings():
    params = parametres()
    fq_in = open(params['arrel_sortida']+'/dicval.pickle','rb')#abrimos el fichero pickle del query
    val = pickle.load(fq_in)
    
    for i in val.keys():
        image_rank = open(params['arrel_sortida']+'/rankings/'+i+'.txt','r')#ficheros de salida
        rank="" 
        for line in image_rank:
            rank=' '.join([rank,line])
        image_rank.close() 
        
        save_ranking_file('rankings', i, rank)
        

def convert_ranking_annotation(annotation_val, annotation_train, file_to_save):

    # Convert ranking annotation and store it for Kaggle (only needed for teachers)

    file_to_save.write('Query,RetrievedDocuments\n')
    for image_id in annotation_val['ImageID']:

        i_class = list(annotation_val.loc[annotation_val['ImageID'] == image_id]['ClassID'])[0]

        if not i_class == 'desconegut':

            file_to_save.write(image_id + ',')
            to_write = annotation_train.loc[annotation_train['ClassID'].isin([i_class])]['ImageID'].tolist()

            for i in to_write:
                file_to_save.write(i + ' ')
            file_to_save.write('\n')

    file_to_save.close()

    print "Done. Annotation file saved"