def calcolaPunti(pedina):
    valori = {'p': 1, 'c': 3, 'a': 3, 't': 5, 'd': 9, 'r': 0}
    return valori.get(pedina.lower(), 0)

def contaPezzi(scacchiera):
    pezzi = {'r': 0, 'd': 0, 'a': 0, 'c': 0, 't': 0, 'p': 0,
             'R': 0, 'D': 0, 'A': 0, 'C': 0, 'T': 0, 'P': 0}
    for riga in scacchiera:
        for cella in riga:
            for pedina in cella:
                if pedina in pezzi:
                    pezzi[pedina] += 1
    return pezzi

def posizioneLegale(scacchiera):
    # Controllo pedoni in prima/ultima riga
    for cella in scacchiera[0] + scacchiera[-1]:
        if 'p' in cella or 'P' in cella:
            return False
    # Controllo numero massimo pezzi
    pezzi = contaPezzi(scacchiera)
    limiti = {'r': 1, 'd': 1, 'a': 2, 'c': 2, 't': 2, 'p': 8,
              'R': 1, 'D': 1, 'A': 2, 'C': 2, 'T': 2, 'P': 8}
    for k in limiti:
        if pezzi[k] > limiti[k]:
            return False
    return True

def valutaMateriale(scacchiera):
    puntiBianchi = 0
    puntiNeri = 0
    for riga in scacchiera:
        for cella in riga:
            for pedina in cella:
                if pedina.islower():
                    puntiBianchi += calcolaPunti(pedina)
                elif pedina.isupper():
                    puntiNeri += calcolaPunti(pedina)
    if puntiBianchi > puntiNeri:
        return 1
    elif puntiNeri > puntiBianchi:
        return 2
    else:
        return 0

def leggiScacchieraDaFile(nomefile):
    scacchiera = []
    with open(nomefile) as f:
        for line in f:
            scacchiera.append(line.strip().split())
    return scacchiera

def valutaPosizione(nomefile):
    scacchiera = leggiScacchieraDaFile(nomefile)
    if not posizioneLegale(scacchiera):
        return -1
    return valutaMateriale(scacchiera)

if __name__ == "__main__":
    for nomefile in ["scacchieraBase.txt", "scacchieraBianca.txt", "scacchieraNera.txt", "scacchieraSbagliata.txt"]:
        risultato = valutaPosizione(nomefile)
        print(f"{nomefile}: {risultato}")