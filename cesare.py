def isValidStr(testo):
    return type(testo)==str and testo.isalpha

def isValidInt(chiave):
    return type(chiave)==int

def cifra(testo,chiave):
    if(not isValidStr(testo) or not isValidInt(chiave)):
        return print("Errore parametri")
    cifrato=""
    for carattere in testo:
        indice=ord(carattere)+chiave
        if(chr(indice)>'z'):
            indice=indice-26
        elif(chr(indice)>'Z' and chr(indice-chiave)<='Z'):
            indice=indice-26
        cifrato+=chr(indice)
    return cifrato

def decifra(testo,chiave):
    if(not isValidStr(testo) or not isValidInt(chiave)):
        return print("Errore parametri")
    decifrato=""
    for carattere in testo:
        indice=ord(carattere)-chiave
        if(chr(indice)<'A'):
            indice=indice+26
        elif(chr(indice)<'a' and chr(indice+chiave)>='a'):
            indice=indice+26
        decifrato+=chr(indice)
    return decifrato

if __name__ == "__main__":
    print("Inserisci del testo: ")
    testo=input()
    print("Inserisci la chiave: ")
    chiave=int(input())
    print("Testo cifrato: ", cifra(testo,chiave))
    print("Testo decifrato: ", decifra(cifra(testo,chiave),chiave))
    if(testo==decifra(cifra(testo,chiave),chiave)):
        print("Funziona")
    else:
        print("Non funziona")