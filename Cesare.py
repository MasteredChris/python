import os

def isString(testo):
    if(not type(testo) == str):
        print("Errore: il testo deve essere una stringa")
    return type(testo) == str

def isValidInt(numero):
    return type(numero) == int and numero >= 0 and numero < 21

def cifra(testo,chiave):
    if(not isString(testo) or not isValidInt(chiave)):
        return "Errore nei parametri(cifratura)"
    risultato=""
    for carattere in testo:
        indice=ord(carattere)+chiave
        if chr(indice)>'z':
            indice=indice-26
        elif chr(indice)>'Z' and chr(indice-chiave)>='A' and chr(indice-chiave)<='Z':
            indice=indice-26
        risultato+=chr(indice)
    return risultato

def decifra(testo,chiave):
    if(not isString(testo) or not isValidInt(chiave)):
        return "Errore nei parametri(decifratura)"
    risultato=""
    for carattere in testo:
        indice=ord(carattere)-chiave
        if chr(indice)<'A':
            indice=indice+26
        elif chr(indice)<'a' and chr(indice+chiave)>='a' and chr(indice+chiave)<='z':
            indice=indice+26
        risultato+=chr(indice)
    return risultato


if __name__ == "__main__":
    print("Inserire un testo in chiaro: ")
    testoInChiaro=input()
    print("Inserire una chiave numerica: ")
    chiave=int(input())
    print("Testo in chiaro: ",testoInChiaro)
    print("Chiave: ",chiave)
    print("Testo cifrato: ",cifra(testoInChiaro,chiave))
    print("Testo decifrato: ",decifra(cifra(testoInChiaro,chiave),chiave))

    if(testoInChiaro==decifra(cifra(testoInChiaro,chiave),chiave)):
        print("Funziona")
    else:
        print("Non funziona")

    input("Premere Invio per pulire il terminale...")
    os.system('cls' if os.name == 'nt' else 'clear')