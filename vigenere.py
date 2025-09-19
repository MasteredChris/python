from cesare import *

def creaValoreChiave(lettera):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    indice=alfabeto.find(lettera)
    return indice

def creaChiave(testo,chiave):
    newKey=""
    while(len(newKey)<len(testo)):
        newKey+=chiave
    return newKey[0:len(testo):1]

def cifraVigenere(testo,chiave):
    cifrato=""
    for i in range(len(testo)):
        carattere=testo[i]
        lettera=chiave[i]
        indice=creaValoreChiave(lettera)
        cifrato+=cifra(carattere,indice)
    return cifrato

def decifraVigenere(testo,chiave):
    decifrato=""
    for i in range(len(testo)):
        carattere=testo[i]
        lettera=chiave[i]
        indice=creaValoreChiave(lettera)
        decifrato+=decifra(carattere,indice)
    return decifrato

if __name__ == "__main__":
    print("Inserisci del testo: ")
    testo=input()
    print("Inserisci la chiave: ")
    chiave=input()
    Key=creaChiave(testo,chiave)
    print("Chiave: ",Key)
    print("Testo cifrato: ", cifraVigenere(testo,Key))
    print("Testo decifrato: ", decifraVigenere(cifraVigenere(testo,Key),Key))
    if(testo==decifraVigenere(cifraVigenere(testo,Key),Key)):
        print("Funziona")
    else:
        print("Non funziona")