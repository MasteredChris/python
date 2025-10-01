      
            
if __name__ == "__main__":
    cifre={"zero":0,"uno":1,"due":2,"tre":3,"quattro":4,"cinque":5,"sei":6,"sette":7,"otto":8,"nove":9}
    f=open("sequenza.txt", "r")
    lines=f.readlines()
    tot=0
    for riga in lines:
        riga=riga.strip().split()
        ris=""
        for num in riga:
            if num in cifre:
                ris+=str(cifre[num])
        if ris!="":
            tot+=int(ris)
    print("La somma dei numeri nella sequenza e':", tot)
    f.close()