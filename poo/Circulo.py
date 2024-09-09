import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        area = math.pi * (self.raio**2)
        return area

    def perimetro(self):
        perimetro = 2 * math.pi * 2 * self.raio
        return perimetro


raio = float(input('Informe o raio do círculo: '))
c1 = Circulo(raio)
print(f'Área:  {c1.area()}')
print(f'Perimetro:  {c1.perimetro()}')