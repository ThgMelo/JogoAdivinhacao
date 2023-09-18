print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************\n')

numero_secreto = 42

total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
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

    rodada += 1

print('\nFim do jogo')
