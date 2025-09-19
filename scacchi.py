from utils import *

def calcolaPunti(pedina):
    #print(pedina)
    if pedina=="T" or pedina=="t":
        return 5
    elif pedina=="C" or pedina=="c":
        return 3
    elif pedina=="A" or pedina=="a":
        return 3
    elif pedina=="D" or pedina=="d":
        return 9
    elif pedina=="P" or pedina=="p":
        return 1
    else:
        return 0
    
def determinaEsito(scacchiera):
    puntiBianchi=0
    puntiNeri=0
    for riga in scacchiera:
        for carattere in riga:
            for i in range(len(carattere)):
                if(carattere[i].islower()):
                    puntiBianchi+=calcolaPunti(carattere[i])
                else:
                    puntiNeri+=calcolaPunti(carattere[i])
    print("Punti Bianco:",puntiBianchi," Punti Nero:",puntiNeri)
    if puntiBianchi>puntiNeri:
        return "Vittoria Bianco"
    elif puntiNeri>puntiBianchi:
        return "Vittoria Nero"
    else:
        return "Parità"

def isValid(scacchiera):
    for riga in scacchiera[0]:
        if riga.find("p")!=-1 or riga.find("P")!=-1:
            return -1
        else: 
            esercito={"r":1,"R":1,"d":1,"D":1,"t":2,"T":2,"a":2,"A":2,"c":2,"C":2,"p":8,"P":8}
            for riga in scacchiera:
                for carattere in riga:
                    for pedina in carattere:
                        for soldato in esercito:
                            if(soldato==pedina):
                                esercito[soldato]-=1
            for soldato in esercito:
                if(esercito[soldato]<0):
                    return -1
            return 0
                
                
if __name__ == "__main__":
    f= openFileForReading("scacchieraBase.txt")
    if f is not None:
        scacchiera=[]
        for line in f:
            riga=line.strip().split()
            scacchiera.append(riga)
        print("Base:",determinaEsito(scacchiera))
        closeFile(f)
        
    f= openFileForReading("scacchieraBianca.txt")
    if f is not None:
        scacchiera=[]
        for line in f:
            riga=line.strip().split()
            scacchiera.append(riga)
        print("Bianco:",determinaEsito(scacchiera))
        closeFile(f)
    
    f= openFileForReading("scacchieraNera.txt")
    if f is not None:
        scacchiera=[]
        for line in f:
            riga=line.strip().split()
            scacchiera.append(riga)
        print("Nero:",determinaEsito(scacchiera))
        closeFile(f)
        
    f= openFileForReading("scacchieraSbagliata.txt")
    if f is not None:
        scacchiera=[]
        for line in f:
            riga=line.strip().split()
            scacchiera.append(riga)
        print("Esito:",isValid(scacchiera))
        closeFile(f)
    
    