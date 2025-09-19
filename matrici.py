from utils import *
if __name__ == "__main__":
    f = openFileForReading("int.txt")
    if f is not None:
        matrix=[]
        fristLine = f.readline()
        for line in f:
            values = line.split()
            if(int(values[0]) != 0):
                matrix.append([int(x) for x in values])
        row=len(matrix)
        col=len(matrix[0])
        print("Righe:",row," Colonne:",col)
        matrix.reverse()
        print(matrix)
        
        firstLine = str(str(row)+"X"+str(col))
        f = openFileForWriting("out.txt")
        if f is not None:
            f.write(str(firstLine)+"\n")
            for r in range(0,row):
                line = ""
                for c in range(0,col):
                    line += str(matrix[r][c])+" "
                f.write(line.strip()+"\n")
        
        closeFile(f)
