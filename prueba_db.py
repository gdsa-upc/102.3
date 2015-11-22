

import os 

def prueba_db(tipo,indir,outdir):
    images = os.listdir(indir) 
    outfile = open(outdir+'/DB_Annotation.txt','w')  
    for file in images:
        outfile.write(file[0:-4]+"\n") 
    outfile.close()

ruta = os.path.dirname(os.path.abspath("__file__"))
prueba_db("train",ruta+'/TerrassaBuildings900/TerrassaBuildings900/train/images',ruta+'/TerrassaBuildings900/TerrassaBuildings900/train')
prueba_db("val",ruta+'/TerrassaBuildings900/TerrassaBuildings900/val/images',ruta+'/TerrassaBuildings900/TerrassaBuildings900/val')