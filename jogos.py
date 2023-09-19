import forca
import adivinhacao

print('***************************')
print('*****Escolha seu jogo!*****')
print('***************************\n')

print('(1) Forca | (2) Adivinhação')

jogo = int(input("Qual jogo? "))

if jogo == 1:
    print('\n\nJogando Forca\n\n')
    forca.jogar()
elif jogo == 2:
    print('\n\nJogando Adivinhação')
    adivinhacao.jogar()