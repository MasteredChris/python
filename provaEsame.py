      
            
if __name__ == "__main__":
    f=open("test_drive.csv", "r")
    lines=f.readlines()
    contNan=0
    contFren=0
    contSec=0
    fren=0
    sec=0
    for riga in lines[1:]:
        riga=riga.strip().split(",")
        if riga[3]=="nan":
            contNan+=1
        else:
            fren+=float(riga[3])
            contFren+=1
        if riga[4]=="nan":
            contNan+=1
        else:
            sec+=float(riga[4])
            contSec+=1
    print("La media della frenata e':", fren/contFren)
    print("La media della distanza di sicurezza e':", sec/contSec)
    print("Il numero di nan e':", contNan)
    f.close()