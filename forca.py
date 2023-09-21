def jogar():
    print('**************************')
    print('Bem vindo ao jogo de Forca!')
    print('**************************\n')

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ["_" for letra in palavra_secreta] # List Comprehension

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input('Qual letra?: ')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f'Ops, você errou! Faltam {6-erros} tentativas!')
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    print('\nFim do jogo')

if __name__ == '__main__':
    jogar()