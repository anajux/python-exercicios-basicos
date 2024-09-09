
#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def dados():
    dado = random.randint(1,6) * 2
    return dado

def craps():
    pontos = 0
    
    if dados() == 7 or dados() == 11:
        print(f'Natural !! Você ganhou!')
    elif dados() == 2 or dados() == 3 or dados() == 12:
        print(f'CRAPS !! Você perdeu!')
    else:
        print(f'Você tem {dados()} pontos. Continue jogando.')
        dados()
        while dados() == proxima_jogada or dados() != 7:
              print(f'Você tem {dados()} pontos. Continue jogando até cair esse valor novamente.')
              proxima_jogada = int(input('Jogue de novo.'))
              
dados() = int(input('Quanto voce tirou na primeira jogada?'))
craps(dados())