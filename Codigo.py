import random
print('JOGO DE ADIVINHAÇÃO')
num = random.randint(0, 5)
print('Escolha um número de 0 à 5')
escolha = int(input('Digite o número que está pensando: '))
if escolha == num:
    print('Parabéns! Você acertou.')
else :
    print('Você errou! Tente novamente.')
