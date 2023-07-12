import random
aleatorio = random.randint(1, 10)
tentativas = 3

while(tentativas != 0):
  escolhido = int(input('Escolha um numero de 1 a 10: '))
  if(aleatorio == escolhido):
    print('Voce acertou!')
    print('Voce ganhou')
    break
  else:
    tentativas -= 1
    print('Voce errou!')
    print(f'Voce tem mais {tentativas} tentativas')
else:
  print('Voce perdeu')
