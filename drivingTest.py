import numpy as np
from fileutils import *

def remove_nan(arr):
    NaNcount = 0
    valori = []
    for x in arr:
        if x.lower() == 'nan':
            NaNcount = NaNcount + 1
        else:
            valori.append(float(x))
    return (valori, NaNcount)

def impostaValoriRiga(intestazione,riga):
    valori = riga.split(',')
    result = {}
    for i in range(0,len(intestazione)):
        result[intestazione[i].strip()] = valori[i].strip()
    return result
    
# NOTA: mi aspetto
# time,evt_type,go,brake_rt,sec_rt,sdlp1,sdlp2,segnum,pathnum,on_exit
def caricaValori(file):
    riga = file.readline()
    intestazione = riga.split(',')
    riga = file.readline()
    risultato = []
    while riga != "":
        valori = impostaValoriRiga(intestazione,riga)
        risultato.append(valori)
        riga = file.readline()
    return risultato

def elabora(filenamein):
    brake_rt = []
    sec_rt = []
    times = []
    try:
        file = apriFileInLettura(filenamein)
    except:
        return("File di input non trovato")
    if file.readable():
        valori = caricaValori(file)
        print(valori)
        for valore in valori:
            times.append(valore['time'])
            sec_rt.append(valore['sec_rt'])
            brake_rt.append(valore['brake_rt'])

        (sec_rt_pulito,secrtnancount) = remove_nan(sec_rt)
        (brake_rt_pulito,brakertnancount) = remove_nan(brake_rt)
        np_times = np.array(times)
        np_brake_rt = np.array(brake_rt)
        np_sec_rt = np.array(sec_rt)

        #missed_brake, brake_rt_no_nan = remove_nan(brake_rt)
        #_, sec_rt = remove_nan(sec_rt)
        Avg_brake_rt = np.mean(brake_rt_pulito)
        Avg_sec_rt = np.mean(sec_rt_pulito)
        
        print("Media dei tempi di frenata: {}, nota che ci sono state {} mancate frenate".format(Avg_brake_rt,brakertnancount))
        print("Media dei tempi di reazione: {}".format(Avg_sec_rt))
        return str(len(valori))


#############################################################
# Eseguo se sono nel main
#############################################################

if __name__ == "__main__":
    filenamein = input("Nome File di input?\r\n")
    result = elabora(filenamein)
    print (result)
    print ("Terminata elaborazione")
