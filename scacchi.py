from utils import *

def calcolaPunti(pedina):
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
    for r in range(0,len(scacchiera)):
        for c in range(0,len(scacchiera[r])):
            punti=calcolaPunti(scacchiera[r][c])
            if scacchiera[r][c].isupper():
                puntiBianchi+=punti
            else:
                puntiNeri+=punti
        print("Punti Bianco:",puntiBianchi," Punti Nero:",puntiNeri)
    if puntiBianchi>puntiNeri:
        return "Vittoria Bianco"
    elif puntiNeri>puntiBianchi:
        return "Vittoria Nero"
    else:
        return "Parità"

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

    