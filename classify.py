import pickle
import random
import numpy as np
labels = ['catedral','mercat_independencia','mnactec','masia_freixa','castell_cartoixa','societat_general','estacio_nord','dona_treballadora','escola_enginyeria','farmacia_albinyana','teatre_principal','ajuntament','desconegut']
def classify (dicc, outdir):
    outfile = open(outdir+'/CL.txt','r+')
    val_id = open(dicc, 'rb')
    mydict = pickle.load(val_id)
    ides=mydict.keys()

    for ids in ides:
        lab=labels[np.random.random_integers(0,12)]
        outfile.write(ids + ' ' + lab+ '\n')
    val_id.close()
    outfile.close()