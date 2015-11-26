# -*- coding: utf-8 -*-
import os

def evaluate_ranking(indir,gtt, gtv):
    f=open(gtt,'r') #obrim el fitxer ground truth del train i llegim l'interior
    lines=f.read().split()
    f.close()
    dic_gtt={} #crea un diccionari amb la ground truth de train
    par=0
    for line in lines:
        if par==0:
            key=line
            par=1
        else:
            par=0
            dic_gtt[key]=line        
    f=open(gtv,'r') #fem el mateix amb els del tes o validació
    lines=f.read().split()
    f.close()
    dic_gtv={} #crea un diccionari amb la ground truth de validació o test
    par=0
    for line in lines:
        if par==0:
            key=line
            par=1
        else:
            par=0
            dic_gtv[key]=line
       
    ranks = os.listdir(indir)  #llegeixo tots els noms dels fitxers del directori d'entrada i els guarda a ranks
    sumap=0 #suma dels average precisions
    contr=0
    for r in ranks:
        #llegeix els resultats de cada rank
        R=r.rstrip('.txt')
        if R!='Thumb':
            contr=contr+1#contador de ranks
            c=dic_gtv[R]
            f=open(indir+'/'+r)
            lines=f.read().split()
            f.close()
            cont=0 #comptador de resultats
            ce=0 #comptador de resultats encertats
            sump=0 #suma de precisions
            for l in lines:
                if l!='Thumb':
                    cont=cont+1
                    if dic_gtt[l]==c:
                        ce=ce+1
                        sump=sump+(float(ce)/float(cont))
            ap=float(sump)/float(ce)
            sumap=float(sumap)+float(ap)
            print r 
            print' average precision='
            print ap 
            print'\n'
    print 'mean average precision='
    print float(sumap)/float(contr)
    print'\n'