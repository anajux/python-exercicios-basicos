
class Pessoa:
    def __init__(self, nome:str, cpf:str, endereco:str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        
class Aluno(Pessoa):
    def __init__(self, nome:str, cpf:str, endereco:str, matricula:str) -> None:
        super().__init__(nome, cpf, endereco)
        self.matricula = matricula
        
class Funcionario(Pessoa):
    def __init__(self, nome:str, cpf:str, endereco:str, codigo:str, salario:float) -> None:
         super().__init__(nome, cpf, endereco)
         self.codigo = codigo
         self.salario = salario
         
class Coordenador(Funcionario):
    def __init__(self)