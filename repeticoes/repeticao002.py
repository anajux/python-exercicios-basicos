
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str (input('Digite seu nome: '))
senha = str (input('Digite sua senha: '))

while nome == senha:
    print('Senha e nome não podem ser iguais. Tente novamente.')
    nome = str (input('Digite seu nome: '))
    senha = str (input('Digite sua senha: '))