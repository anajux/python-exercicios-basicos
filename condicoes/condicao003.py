
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = str(input('Informe F/M: '))

genero = genero.upper()

if genero == "F":
    print('F - Feminino.')
    
elif genero == "M":
    print('M - Masculino')
    
else:
    print('Sexo inválido.')