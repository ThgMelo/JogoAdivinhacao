def jogar():
    print('**************************')
    print('Bem vindo ao jogo de Forca!')
    print('**************************\n')

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input('Qual letra?: ')
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f"Encontrei a letra {chute} na posição {index}")
            index += 1

        print("jogando...")

    print('\nFim do jogo')

if __name__ == '__main__':
    jogar()