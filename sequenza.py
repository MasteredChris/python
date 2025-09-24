from utils import *

if __name__=="__main__":
    cifre={"zero":0,"uno":1,"due":2,"tre":3,"quattro":4,"cinque":5,"sei":6,"sette":7,"otto":8,"nove":9}
    somma=0
    filename=input("Nome del file di input: ")
    f=openFileForReading(filename)
    if f is not None:
        for riga in f:
            numeri=riga.strip().split()
            risultato=""
            for n in numeri:
                if n in cifre:
                    risultato+=str(cifre[n])
                elif n=="stop":
                    print(risultato)
                    if risultato!="":
                        somma+=int(risultato)
                    risultato=""
                else:
                    print("Parola non valida: "+n)
        f.close()
        print("Somma totale: "+str(somma))