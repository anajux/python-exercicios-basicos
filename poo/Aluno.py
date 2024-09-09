
#Implemente uma classe chamada “Aluno” que possua atributos para armazenar o nome, a matrícula e as notas de um aluno. 
# Adicione métodos para calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado).

class Aluno:
    def __init__(self, nome, matricula, nota1, nota2):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        
    def media(self):
        soma = self.nota1 + self.nota2
        media = soma/2
        return media
    
a1 = Aluno("Joao", 2022333, 10, 9.6)
print(a1.media())
print(a1.nome)
    