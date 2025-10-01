if __name__ == "__main__":
    f=open("int.txt", "r")
    lines=f.readlines()
    intestazione=lines[0].strip()
    intestazione=intestazione.split("X")
    intestazione = list(map(int, intestazione))
    righe=[]
    for line in lines[1:]:
        if int(line[0])==0:
            intestazione[0]-=1
        else:
            righe.append(line.strip())
    print("{}X{}".format(intestazione[0], intestazione[1]))
    righe.reverse()
    for val in righe:
        print(val)
    f.close()