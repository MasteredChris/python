from utils import *

if __name__=="__main__":
    coordinate={"x":0,"y":0}
    isValid=True
    f=openFileForReading("spostamenti.txt")
    if f is not None:
        for riga in f:
            move=riga.strip().split()
            if(move[0]=="N"):
                coordinate["y"]+=int(move[1])
            elif(move[0]=="S"):
                coordinate["y"]-=int(move[1])
            elif(move[0]=="E"):
                coordinate["x"]+=int(move[1])
            elif(move[0]=="O"):
                coordinate["x"]-=int(move[1])
            else:
                isValid=False
                print("Direzione non valida: "+move[0])

        f.close()
        
        if isValid:
            if(coordinate["y"]>0):
                y_label = "Nord:"
                y_val = str(coordinate["y"])
            elif(coordinate["y"]<0):
                y_label = "Sud:"
                y_val = str(abs(coordinate["y"]))
            else:
                y_label = "Y:"
                y_val = "0"

            if(coordinate["x"]>0):
                x_label = "Est:"
                x_val = str(coordinate["x"])
            elif(coordinate["x"]<0):
                x_label = "Ovest:"
                x_val = str(abs(coordinate["x"]))
            else:
                x_label = "X:"
                x_val = "0"

            result = y_label + " " + y_val + "\r\n" + x_label + " " + x_val
            print(result)   
        