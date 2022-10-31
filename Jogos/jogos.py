import forca
import advinhacao


def menu():
    opcao = 0

    print('*********************')
    print('**Escolha seu jogo!**')
    print('*********************')

    print('(1) Forca\n'
          '(2) Advinhacao')

    opcao = int(input('Qual Jogo? '))

    if opcao == 1:
        print('Jogando Forca\n\n')
        forca.jogar()
    elif opcao == 2:
        print('Jogando Advinhacao\n\n')
        advinhacao.jogar()


if __name__ == "__main__":
    menu()

