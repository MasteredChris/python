from cesare import *

def cifra(testobase,chiavebase):
    """implementa il cifrario di vigenere, ricordare di mettere un testo come chiave"""
    if not (validoTestoXCesare(testobase) and validoTestoXCesare(chiavebase)):
        return _errore_nei_parametri
    chiave = armonizza(testobase,chiavebase) #mi accerto che abbia la stessa lunghezza
    risultato = ""
    testo = testobase.lower()
    for i in range(0,len(testo)):
        inChiaro = testo[i]
        charChiave = chiave[i];
        intChiave = ord(charChiave) - charA
        criptato = cifraCesare(inChiaro,intChiave)
        risultato += criptato
    return risultato

def decifra(cifratobase,chiavebase):
    """implementa il cifrario di vigenere, ricordare di mettere un testo come chiave"""
    if not (validoTestoXCesare(cifratobase) and validoTestoXCesare(chiavebase)):
        return _errore_nei_parametri
    chiave = armonizza(cifratobase,chiavebase) #mi accerto che abbia la stessa lunghezza
    risultato = ""
    cifrato = cifratobase.lower()
    for i in range(0,len(cifrato)):
        cifra = cifrato[i]
        charChiave = chiave[i];
        intChiave = ord(charChiave) - charA
        inchiaro = decifraCesare(cifra,intChiave)
        risultato += inchiaro
    return risultato

#####################################################################################################
# se siamo nel main
#####################################################################################################
if __name__ == "__main__":
        print("Verifica dei metodi di cifratura")
        inChiaro =  "CiaoDoveAndiamoOggi"
        chiave = "claudio"
        #####
        cifrato = cifra(inChiaro,chiave)
        decifrato = decifra(cifrato,chiave)
        verificaVigenere = inChiaro.lower() == decifra(cifra(inChiaro,chiave),chiave)
        print("Verifica dei metodi cifra() e decifra(): esito", str(verificaVigenere))
        print(inChiaro.lower()," [vigenere(",chiave,")]-> ",cifrato, " -> ",decifrato)

