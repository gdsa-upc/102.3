import pickle
import random

labels = ['catedral','mercat_independencia','mnactec','masia_freixa','castell_cartoixa','societat_general','estacio_nord','dona_treballadora','escola_enginyeria','farmacia_albinyana','teatre_principal','ajuntament','desconegut']
line=1

def classify (valors_id, outdir):
    f=open(outdir,"w")
    val_id = open(valors_id, 'rb')
    mydict = pickle.load(val_id)
    val_id.close()
    print mydict
    ides=mydict.keys()

    for ids in ides:
            for line in len(labels):
                f.write(ids + ":" + labels[random.choice(15)] + '\n')
                if line ==15:
                    line=1
                else : 
                    line = line+1
    f.close()
    print f
        
            
        

    


#for line in lines:
#  diccionari[line.split(" ")[0]]=line.split(" ")[1]
 #   print diccionari
    
    