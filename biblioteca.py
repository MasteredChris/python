def getTupla(riga):
    riga=riga.strip().split(";")
    return tuple(riga)

if __name__ == "__main__":
    f=open("biblioteche_.csv", "r")
    lines=f.readlines()
    intestazione=lines[0].strip()
    tupla=getTupla(intestazione)
    comune=input("Inserisci il nome del comune: ").lower()
    righe=[]
    cont=0
    for riga in lines[1:]:
        riga=riga.strip().split(";")
        if riga[2].lower()==comune:
            righe.append(riga)
            cont+=1
    for riga in righe:
        for elem in riga:
            print(elem, end=",")
        print("\n")
    print("Numero di biblioteche nel comune di", comune, ":", cont)
    print(tupla)
    f.close()