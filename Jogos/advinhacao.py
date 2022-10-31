import random
import jogos


def jogar():
    print('*******************************')
    print('Bem Vindo ao Jogo de Advinhacao')
    print('*******************************')

    numero_secreto = random.randrange(1, 101)

    print('Selecione a dificuldade ')
    print('(1) Facil\n(2) Medio\n(3) Dificil')
    opcao = int(input(''))

    if opcao == 1:
        tentativas = 10
    elif opcao == 2:
        tentativas = 7
    else:
        tentativas = 5

    for tentativas in range(tentativas, 0, -1):
        chute = int(input('Digite um numero entre 1 e 100 '))

        if (chute < 1 or chute > 100):
            print(f'Tentativas restantes {tentativas - 1}\n')
            continue

        diferenca = numero_secreto - chute

        if diferenca == 0:
            print('Voce acertou')
            break
        elif diferenca > 0:
            print('O numero secreto e maior que o chute')
            print('Tente novamente\n')
            print(f'Tentativas restantes {tentativas - 1}')

        else:
            print('O numero secreto e menor que o chute')
            print('Tente novamente\n')
            print(f'Tentativas restantes {tentativas - 1}')

    print('Fim de jogo')
    print('O numero secreto era ', numero_secreto)
    jogos.menu()


if __name__ == "__main__":
    jogar()
