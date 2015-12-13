# -*- coding: utf-8 -*-
import pickle 
from Parametres import parametres
import warnings
warnings.filterwarnings("ignore")
def classify():
    params = parametres()
    bow_val = pickle.load( open('/'.join([params['arrel_sortida']+'/dicval.pickle']), "r" ))#cargamos features a bow_val
    classifier= pickle.load( open(params['arrel_sortida']+'/model_classifier.pickle', 'r') )#cargamos el clasificador entrenado
    outfile = open(params['arrel_sortida']+'/classification.txt', 'wb')#creamos directorio de salida
    #print bow_val
    for im_id, im_bow in bow_val.items():
        outfile.write(str(im_id) + "\t" + str(classifier.predict(im_bow)[0]) + "\n"  ) # escribimos la id de la imagen con la predicción del clasificador
    outfile.close()
