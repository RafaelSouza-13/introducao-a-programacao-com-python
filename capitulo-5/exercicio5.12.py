from decimal import Decimal
deposito = float(input('Digite o deposito inicial: '))
taxa = float(input('Digite a taxa de juros: '))
deposito_mes = float(input('Digite o valor de deposito mensal: '))
acumulador = deposito
mes = 1
while(mes <= 24):
  resultado = (acumulador * taxa) / 100
  print(f'Mês {mes}: {acumulador:.2f} * {taxa} = {(acumulador + resultado):.2f}')
  acumulador += resultado
  mes += 1
  acumulador += deposito_mes

print(f'Valor depositado: {deposito} \n Taxa de juros: {taxa} \n Total de ganho em 24 meses = {(acumulador - deposito):.2f} \n valor total: {acumulador:.2f}')