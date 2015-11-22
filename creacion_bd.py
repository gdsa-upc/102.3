import os 
def creacion_bd(tipo,indir,outdir):
    images = os.listdir(indir) 
    outfile = open(outdir+'/DB_Annotation.txt','w')  
    for file in images:
        outfile.write(file[0:-4]+"\n") 
    outfile.close()
ruta = os.path.dirname(os.path.abspath("__file__"));
creacion_bd("train",ruta+'/TerrassaBuildings900/TerrassaBuildings900/train/images',ruta+'/TerrassaBuildings900/TerrassaBuildings900/train');
creacion_bd("val",ruta+'/TerrassaBuildings900/TerrassaBuildings900/val/images',ruta+'/TerrassaBuildings900/TerrassaBuildings900/val');