from numpy import *
import numpy as np

if __name__ == "__main__":
    f=open("test_drive.csv","r",encoding="utf-8")
    lines=f.readlines()
    lines=lines[1:]  # skip header
    nan=0
    mFren=0
    cont=0
    for line in lines:
        riga=line.strip().split(",")
        if riga[4]=="nan":
            nan+=1
        if riga[3]=="nan":
            nan+=1
        else:
            mFren+=float(riga[3])
            cont+=1
    print(mFren)
    print("Media frequenza:",mFren/cont)
    print("Nan:",nan)
    f.close()