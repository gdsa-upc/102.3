import open
import pickle

labels = ['catedral','ajuntament','desconegut']
line=1

def classify (outdir):
    f=open(outdir,"w")
    pkl_file = open('Val_diccionari.pkl', 'rb')
    mydict = pickle.load('Val_diccionari')
    pkl_file.close()
    print mydict

    ides=mydict.keys()

    for ids in ides:
    for line in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        f.write(ids + ":" + labels[line] + "\n")
        if line ==15:
            line=1
            else     line = line+1
            
        

    


for line in lines:
    diccionari[line.split(" ")[0]]=line.split(" ")[1]
    print diccionari
    
    