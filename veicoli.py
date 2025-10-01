# Classe base
class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrizione(self):
        return f"{self.anno} {self.marca} {self.modello}"
    
# Sottoclasse Auto
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    def descrizione(self):
        return f"{self.anno} {self.marca} {self.modello}  - {self.tipo}"

# Sottoclasse Moto
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    def descrizione(self):
        return f"{self.anno} {self.marca} {self.modello}  - tipo: {self.tipo}"

# Programma principale
if __name__ == "__main__":
    marca = input()
    modello = input()
    anno = int(input())
    tipo = input()
    
    auto1 = Auto(marca,modello,anno,tipo)
    marca = input()
    modello = input()
    anno = input()
    tipo = input()
    
    moto1 = Moto(marca,modello,anno,tipo)

    print(auto1.descrizione())
    print(moto1.descrizione())
