from Cesare import *
def generaValoreLettera(letter):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    return alfabeto.find(letter.lower())

def generaChiave(testo,chiave):
    chiaveGenerata = ""
    chiave = chiave.lower()
    while len(chiaveGenerata) < len(testo):
        chiaveGenerata += chiave
    chiaveGenerata = chiaveGenerata[:len(testo)]
    return chiaveGenerata


def cifraVigenere(testo,chiave):
    testoCifrato = ""
    for i in range(len(testo)):
        letteraTesto = testo[i]
        letteraChiave = chiave[i]
        valoreLetteraChiave = generaValoreLettera(letteraChiave)
        testoCifrato += cifra(str(letteraTesto), int(valoreLetteraChiave))
    return testoCifrato

def decifraVigenere(testo,chiave):
    testoDecifrato = ""
    print("lunghezza testo:",len(testo))
    for i in range(len(testo)):
        letteraTesto = testo[i]
        letteraChiave = chiave[i]
        valoreLetteraChiave = generaValoreLettera(letteraChiave)
        testoDecifrato += decifra(letteraTesto, valoreLetteraChiave)
    return testoDecifrato
        

if __name__ == "__main__":
    print("Inserire un testo in chiaro: ")
    testoInChiaro=input()
    print("Inserire una chiave letterale: ")
    chiave=input()
    nuovaChiave=generaChiave(testoInChiaro,chiave)
    
    print("Testo in chiaro: ",testoInChiaro)
    print("Chiave: ",nuovaChiave)
    
    print("Testo cifrato: ",cifraVigenere(testoInChiaro,nuovaChiave))
    print("Testo decifrato: ",decifraVigenere(cifraVigenere(testoInChiaro,nuovaChiave),nuovaChiave))

    if(testoInChiaro==decifraVigenere(cifraVigenere(testoInChiaro,nuovaChiave),nuovaChiave)):
        print("Funziona")
    else:
        print("Non funziona")

    input("Premere Invio per pulire il terminale...")
    os.system('cls' if os.name == 'nt' else 'clear')