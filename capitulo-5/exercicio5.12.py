from decimal import Decimal
deposito = Decimal(input('Digite o deposito inicial: '))
taxa = Decimal(input('Digite a taxa de juros: '))
deposito_mes = Decimal(input('Digite o valor de deposito mensal: '))
acumulador = deposito
mes = 1
while(mes <= 24):
  resultado = (acumulador * taxa) / 100
  print(f'Mês {mes}: {acumulador:.2f} * {taxa} = {(acumulador + resultado):.2f}')
  acumulador += resultado
  mes += 1
  acumulador += deposito_mes

print(f'Valor depositado: {deposito} \nTaxa de juros: {taxa} \nTotal de ganho em 24 meses = {(acumulador - deposito):.2f} \nvalor total: {acumulador:.2f}')