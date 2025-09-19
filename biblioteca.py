from utils import *

def getTupla(line):
    values = line.split(";")
    return (values[0],values[1],values[2],values[3],values[4].strip())

if __name__ == "__main__":
    print("Inserisci comune:")
    comune=input().lower()
    f= openFileForReading("biblioteche_.csv")
    if f is not None:
        fisrtLine = getTupla(f.readline())
        print("Campi del file:",fisrtLine)
        result=[]
        for line in f:
            riga=line.strip().split(";")
            if(riga[3].lower()==comune.lower()):
                result.append(line)
        for i in range(len(result)):
            print(result[i].strip())
        print("Trovate",len(result),"biblioteche nel comune di",comune)
        closeFile(f)
            
         