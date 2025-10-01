class FiguraGeometrica:

    def area(self):

        return('metodo area non implementato')

    def perimetro(self):

        return('metodo perimetro non implementato')

    def __str__(self):
        return "Figura geometrica generica"
    
class Cerchio(FiguraGeometrica):

    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        import math
        return math.pi * self.raggio * self.raggio

    def perimetro(self):
        import math
        return 2 * math.pi * self.raggio

    def __str__(self):
        return "Cerchio di raggio {}".format(self.raggio)
    
class Quadrato(FiguraGeometrica):
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato * self.lato

    def perimetro(self):
        return 4 * self.lato

    def __str__(self):
        return "Quadrato di lato {}".format(self.lato)

class Rettangolo(FiguraGeometrica):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

    def __str__(self):
        return "Rettangolo di base {} e altezza {}".format(self.base, self.altezza)
    
if __name__ == "__main__":
    listafigure = [FiguraGeometrica(), Cerchio(1.0),Quadrato(1.0),Rettangolo(1.0,2.0)]
    for figura in listafigure:
        print(figura)
        print("Area: {}".format(figura.area()))
        print("Perimetro: {}".format(figura.perimetro()))
        print()