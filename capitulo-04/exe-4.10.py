quantidade_kWh = int(input('Digite a quantidade de kWh consumida: '))
tipo = input('Tipo de instalação \n R - residencias \n I - industrias \n C - comercios \n tipo: ')
tipo = tipo.strip().lower()


if(tipo == 'r'):
  if(quantidade_kWh <= 500):
    valor = quantidade_kWh * 0.40
  else:
    valor = quantidade_kWh * 0.65
elif(tipo == 'c'):
  if(quantidade_kWh <= 1000):
    valor = quantidade_kWh * 0.55
  else:
    valor = quantidade_kWh * 0.60
elif(tipo == 'i'):
  if(quantidade_kWh <= 5000):
    valor = quantidade_kWh * 0.55
  else:
    valor = quantidade_kWh * 0.60
else:
  print('Tipo de instalação invalido!')

try:
  print(f'Valor a pagar: {valor:.2f} R$')
except NameError:
  print('Não foi possivel calcular o valor!')
