from utils import *

if __name__=="__main__":
    f=openFileForReading("uguaglianze.txt")
    somma_dx=0
    somma_sx=0
    righe=0
    corrette=0
    if f is not None:
        for riga in f:
            riga=riga.strip()
            riga=riga.strip(";")
            if "=" in riga:
                righe+=1
                parti=riga.split("=")
                dx=parti[0].strip().split("+")
                sx=parti[1].strip().split("+")
                for cifre in dx:
                    somma_dx+=int(cifre)
                for cifre in sx:
                    somma_sx+=int(cifre)
                if somma_dx==somma_sx:
                    print("vero")
                    corrette+=1
                else:
                    print("falso")
            else:
                print("errore nella riga: "+riga)
        print("frazione di uguaglianze corrette: "+str(corrette)+"/"+str(righe))
        f.close()