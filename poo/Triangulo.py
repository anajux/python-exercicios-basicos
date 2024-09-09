
#lado3rie uma classe chamada “Triângulo” com atributos para armazenar os três lados do triângulo. 
# Implemente métodos para verificar se é um triângulo válido e calcular sua área.

import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def validar_triangulo(self):
        if self.lado1 + self.lado2 > self.lado3 and self.lado2 + self.lado3 > self.lado1 and self.lado1 + self.lado3 > self.lado2:
            if self.lado1 == self.lado2 == self.lado3:
                return "Triângulo Equilátero"
            elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
                return "Triângulo Isósceles"
            else:
                return "Triângulo Escaleno"
            
        else:
            return "Não é um triângulo válido"
        
    def area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 3
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        
        return area
    
t1 = Triangulo(10,13,15)
print(t1.validar_triangulo(), t1.area())