# -*- coding: utf-8 -*-
import os 
def build_database (indir,outdir): #definim la funció
    images = os.listdir(indir)  #llegeixo tots els noms dels fitxers del directori d'entrada i els guarda a images
    outfile = open(outdir+'/ID.txt','w')   #crea el fitxer on escriu els id.
    for file in images: #recorre tots els id i els escriu al fitxer
        outfile.write(file[0:-4]+"\n") 
    outfile.close()#tanca el fitxer