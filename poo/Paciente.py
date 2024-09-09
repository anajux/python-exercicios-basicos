
#Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a idade e o histórico de consultas de um paciente. 
# Implemente métodos para adicionar uma nova consulta ao histórico e exibir as consultas realizadas.

class Paciente:
    def __init__(self, nome, idade, historico = 0.0):
        self.nome = nome
        self.idade = idade
        self.historico = historico
        
    def nova_consulta(self):
        self.historico += 1
    
    def exibir(self):
        print(f'{self.historico} consultas já foram realizadas com o paciente {self.nome}')
    
p1 = Paciente('Julia', 19)
p1.nova_consulta()
print(p1.exibir())
print(p1.idade)