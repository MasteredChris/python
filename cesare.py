
_errore_nei_parametri = "Errore, parametri non validi"
charA = ord('a')
charZ = ord('z')
lenAlfabeto = charZ-charA

def validoTestoXCesare(param):
    if type(param) != str:
        return False
    elif not param.isalpha():
        return False
    return True

def validaChiaveXCesare(param):
    if type(param) != int:
        return False
    elif param < 0 or param > (charZ-charA):
        return False
    return True

def armonizza(testo,chiave):
    if not (validoTestoXCesare(testo) and validoTestoXCesare(chiave)):
        return -1
    lenTesto = len(testo)
    lenChiave = len(chiave)
    if(lenChiave > lenTesto):
        return chiave
    else:
        moltiplicatore = round(lenTesto / lenChiave) + 1
        result = chiave * moltiplicatore
        result = result[0:lenTesto]
        return result
    
def validaXCesare(testobase,chiave):
    """verifica che il testo sia una stringa e che la chiave sia un int
        e che sia una lettera dell'alfabeto"""
    testobaseOK = validoTestoXCesare(testobase)
    chiaveOK = validaChiaveXCesare(chiave)
    result = testobaseOK and chiaveOK
    return result

def cifraCesare(testobase,chiave):
    """implementa il cifrario di cesare, ricordare di mettere un numero come chiave"""
    if not validaXCesare(testobase,chiave):
                return _errore_nei_parametri
    risultato = ""
    testo = testobase.lower()
    for carattere in testo:
        indice = ord(carattere) + chiave
        if indice > charZ:
            indice = indice - lenAlfabeto
        risultato += chr(indice)
    return risultato
    
def decifraCesare(testocriptato,chiave):
    """implementa il cifrario di cesare, la decifrazione"""
    if not validaXCesare(testocriptato,chiave):
                return _errore_nei_parametri
    risultato = ""
    criptato = testocriptato.lower()
    for carattere in criptato:
        indice = ord(carattere) - chiave
        if indice < charA:
            indice = indice + lenAlfabeto
        risultato += chr(indice)
    return risultato

#####################################################################################################
# se siamo nel main
#####################################################################################################
if __name__ == "__main__":
        print("Verifica dei metodi di cifratora")
        inChiaro =  "zzz"
        chiaveCesare = 20
        #####
        cifrato = cifraCesare(inChiaro,chiaveCesare)
        decifrato = decifraCesare(cifrato,chiaveCesare)
        verificaCesare = inChiaro.lower() == decifraCesare(cifraCesare(inChiaro,chiaveCesare),chiaveCesare)
        print("Verifica dei metodi () e decifraCesare(): esito", str(verificaCesare))
        print(inChiaro.lower()," [cesare(",chiaveCesare,")]-> ",cifrato, " -> ",decifrato)
        
