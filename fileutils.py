def apriFileInLettura(filename):
    file = open(filename,'r',encoding="utf-8")
    return file

def apriFileInScrittura(filename):
    file = open(filename,'w',encoding="utf-8")
    return file

def chiudiFile(file):
    file.flush()
    file.close()
    return 
