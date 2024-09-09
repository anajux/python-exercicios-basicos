
#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Nome: '))
while len(nome) < 3:
    print('Nome com menos de 3 caracteres, tente novamente.')
    nome = str(input('Nome: '))

idade = int(input('Idade: '))
while 0 > idade > 150:
    print('Idade não verdadeira. Tente novamente.')
    idade = int(input('Idade: '))
    
salario = float(input('Salário: '))
while salario == 0:
    print ('Não é possível cadastrar esse valor de salário. Tente novamente.')
    salario = float(input('Salário: '))
    
sexo = str (input('Feminino(F)/Masculino(M): ')).upper()
while sexo != 'F' and sexo != 'M':
    print('Sexo inválido. Tente novamente.')
    sexo = str (input('Feminino(F)/Masculino(M): ')).upper()

estadoCivil = str (input('Estado Civil S/C/V/D: ')).upper()
while estadoCivil != 'S' and estadoCivil != 'C' and estadoCivil!= 'V' and estadoCivil != 'D':
    print('Estado Civil inválido. Tente novamente.')
    estadoCivil = str (input('Estado Civil S/C/V/D: ')).upper()
    
print('Concluído.')
    