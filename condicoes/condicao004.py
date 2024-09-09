
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Informe uma letra: '))

letra = letra.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('{} é uma vogal.'.format(letra))
elif letra == 'b' or letra == 'c' or letra == 'd' or letra == 'f' or letra == 'g'or letra == 'h'or letra == 'j'or letra == 'k' or letra =='l' or letra =='m'or letra =='n'  or letra =='p' or letra =='q'or letra =='r'or letra =='s' or letra =='t'or letra =='v' or letra =='w'or letra =='x' or letra =='y' or letra =='z':
    print('{} é uma consoante'.format(letra))
else:
    print('{} é outro tipo de caractere.'.format(letra))
    
    