velocidade = int(input('Digite a velocidade em km/h: '))

if(velocidade > 80):
  multa = 5 * (velocidade - 80)
  print(f'Multa: {multa} R$')