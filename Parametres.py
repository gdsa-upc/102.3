# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as p

def parametres():
    
    params = { }

#inputs
    params['arrel_entrada']='E:/universidad/GDSA/proyecto'
    params['bd_imatges']='Terrassabuildings900/Terrassabuildings900'

#output
    params['arrel_sortida']='E:/universidad/GDSA/proyecto/carpeta de pruebas'
    crea_dirs(params)

#params
    params['mida_descriptor']=10
    identificacions=p.read_csv('E:/universidad/GDSA/proyecto/TerrassaBuildings900/TerrassaBuildings900/train/annotation.txt', sep='\t', header = 0)
#Copieu el path sencer igual que he fet jo perquè la funció read_csv posa les / al revés i no reconeix el path

#identificacions conté tot el fitxer annotation.txt (classificat en id's i noms d'edificis)
    params['Possibles_edificis']=np.unique(identificacions['ClassID'])
#possibles_edificis conté els noms de les 13 possibles categories (12 edificis i desconegut)

    

    return params

#crea_nou_dir: si el directori no exixteix, el crea
def crea_nou_dir(directori):
    if not os.path.isdir(directori):
        os.makedirs(directori)

#crea_dirs: crea tots els directoris que es necessiten i no existeixen cridant 'crea_nou_dir'
def crea_dirs(params):

    dir_out = os.path.join(params['arrel_sortida'])
    crea_nou_dir(dir_out)
    crea_nou_dir(os.path.join(dir_out,'llista_imgs'))
    crea_nou_dir(os.path.join(dir_out,'features'))
    crea_nou_dir(os.path.join(dir_out,'rankings'))
    crea_nou_dir(os.path.join(dir_out,'classificacions'))


#print parametres()