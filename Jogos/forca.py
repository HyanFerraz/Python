import jogos


def jogar():
    print('*******************************')
    print('Bem Vindo ao Jogo de Forca')
    print('*******************************')

    enforcado = False
    acertou = False

    palavra_secreta = "lubellion"

    while not enforcado and not acertou:

        chute = input('\nDigite uma letra ')

        index = 1
        for letra in palavra_secreta:
            if chute == letra:
                print(f'A letra {chute} foi encontrada na(s) posicoes {index}')
            index += 1

    print('Fim de Jogo')
    jogos.menu()


if __name__ == "__main__":
    jogar()
