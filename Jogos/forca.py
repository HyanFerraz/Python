import jogos


def jogar():
    print('*******************************')
    print('Bem Vindo ao Jogo de Forca')
    print('*******************************')

    enforcado = False
    acertou = False

    palavra_secreta = "lubellion"
    letras_acertadas = []
    chances = 6

    for letra in palavra_secreta:
        letras_acertadas.append('_')

    while not enforcado and not acertou:

        for index in range(len(letras_acertadas)):
            print(letras_acertadas[index], end='')

        chute = input('\nDigite uma letra ')
        index = 0

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute.lower() == letra.lower():
                    letras_acertadas[index] = chute
                index += 1
        elif chute not in palavra_secreta:
            print(f'A palavra secreta nao tem a letra {chute}')
            chances -= 1
            print(f'Chances restantes {chances}')

        if chances == 0:
            enforcado = True

        if '_' not in letras_acertadas:
            acertou = True

    print('\nA palavra secreta e', palavra_secreta)
    print('\nFim de Jogo\n')
    jogos.menu()


if __name__ == "__main__":
    jogar()
