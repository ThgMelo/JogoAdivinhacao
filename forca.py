import random

def jogar():
    
    imprimi_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print(f'Ops, você errou! Faltam {6-erros} tentativas!')
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprimi_mensagem_vencedor()
    else:
        imprimi_mensagem_perdedor()
        print('Você perdeu!')


def imprimi_mensagem_abertura():
    print('**************************')
    print('Bem vindo ao jogo de Forca!')
    print('**************************\n')

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', "r") # r = modo leitura
    palavras = []

    for linha in arquivo:
        linha = linha.strip() # apaga o \n
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta =  palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input('Qual letra?: ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1

def imprimi_mensagem_vencedor():
    print('Você ganhou!')

def imprimi_mensagem_perdedor():
    print('Você perdeu!')

if __name__ == '__main__':
    jogar()