
#Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e a altura. 
# Implemente métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        area = self.altura * self.largura
        return area
    
    def perimetro(self):
        perimetro = 2 * (self.altura + self.largura)
        return perimetro
    

r1 = Retangulo(10, 5)
print(r1.largura)