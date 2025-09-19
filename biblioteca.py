from utils import *

def getTupla(line):
    values = line.split(";")
    return tuple(values)

if __name__ == "__main__":
    print("Inserisci comune:")
    comune=input().lower()
    f= openFileForReading("biblioteche_.csv")
    if f is not None:
        fisrtLine = getTupla(f.readline())
        result=[]
        for line in f:
            riga=line.strip().split(";")
            if(riga[3].lower()==comune.lower()):
                result.append(riga[1])
        for i in range(len(result)):
            print(result[i].strip())
        print("\nTrovate",len(result),"biblioteche nel comune di",comune,"\n")
        print("Campi del file:")
        for s in fisrtLine:
            print(" ",s)

        closeFile(f)
            
         