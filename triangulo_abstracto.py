

from figuras_geometricas_abstractas import FiguraGeometrica


class triangulo(FiguraGeometrica):
    def __init__(self, base:float=0.0, alto:float=0.0):
        super().__init__(base=base, alto=alto)


    def __str__(self):
        return f'triangulo [base = {self.base}, alto= {self.alto}]'

    def calcular_area(self):
        return (self.base * self.alto) /2

    def calcular_perimetro(self):
        return 3 * self.alto

if __name__ == '__main__':
    t1 =  triangulo(base=2, alto=5)
    print (t1)
    print(f'El área del triangulo es: {t1.calcular_area()}')
    print(f'El perimetro del triangulo es: {t1.calcular_perimetro()}')