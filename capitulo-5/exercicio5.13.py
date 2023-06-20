from decimal import Decimal
divida = Decimal(input('Valor inicial da divida: '))
taxa_juros = Decimal(input('Valor do juros mensal: '))
valor_mensal = Decimal(input('Valor mensal a ser pago: '))
meses = 0
juros_total = 0
valor_total_pago = 0

while(divida > 0):
  acressimo_juros = (divida * taxa_juros) / 100
  divida += acressimo_juros
  juros_total += acressimo_juros
  meses += 1
  if(valor_mensal < divida): 
    divida -= valor_mensal
    valor_total_pago += valor_mensal
  else:
    valor_total_pago += divida
    divida = 0
    

print(f'Total de meses a ser pago: {meses}, juros: {juros_total:.2f}, total pago: {valor_total_pago:.2f}')