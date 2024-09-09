
#Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o modelo e a velocidade atual do carro. 
# Adicione métodos para acelerar, frear e exibir a velocidade atual.

class Carro:
    def __init__(self, marca, modelo, velocidade = 0.0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
        
    def acelerar(self, acelerador):
        self.velocidade += acelerador
        #return self.velocidade
    
    def frear(self):
        self.valocidade = 0
        #return self.velocidade

    def exibir(self):
        print(f'A velocidade atual é {self.velocidade} km/h')
        #return self.velocidade
        

c1 = Carro('chevrolet', 'onix', 150)
print(c1.acelerar(10))
print(c1.exibir())