
#Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o salário e o cargo do funcionário. 
# Implemente métodos para calcular o salário líquido, considerando descontos de impostos e benefícios.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def salario_liquido(self):
        if self.salario <= 2000:
            salarioLiquido = self.salario - 150
        elif self.salario <= 3000:
            salarioLiquido = self.salario - 300
        else:
            salarioLiquido = self.salario - 220
            
        return salarioLiquido
    
f1 = Funcionario("Julia", 2000, "gdp")
print(f1.salario_liquido())