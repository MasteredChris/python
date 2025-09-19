def openFileForReading(filename):
    try:
        f = open(filename, "r", encoding="utf-8")
        return f
    except IOError:
        print("Error: File does not appear to exist.")
        return None

def openFileForWriting(filename):
    try:
        f = open(filename, "w", encoding="utf-8")
        return f
    except IOError:
        print("Error: File does not appear to exist.")
        return None

def closeFile(file):
    file.flush()
    file.close()
    return
