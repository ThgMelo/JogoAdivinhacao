print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************\n')

numero_secreto = 42

chute_str = int(input('Digite o seu numero: '))

print('Você digitou ', chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print('Você acertou!')
else:
    if maior:
        print('Você errou! O seu chute foi maior que o número secreto.')
    elif menor:
        print('Você errou! Seu chute foi menor que o número secreto')
print('\nFim do jogo')
