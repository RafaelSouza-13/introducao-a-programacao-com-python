from decimal import Decimal
valor = Decimal(input('Digite o valor a pagar: '))
cedulas = 0
atual = 100
apagar = valor

while True:
  if atual <= apagar:
    apagar -= atual
    cedulas += 1
  else:
    print(f'{cedulas} cédulas(s) de RS{atual}')
    if apagar == 0:
      break
    if atual == 100:
      atual = 50
    elif atual == 50:
      atual = 20
    elif atual == 20:
      atual = 10
    elif atual == 10:
      atual = 5
    elif atual == 5:
      atual = 1
    elif atual == 1:
      atual = apagar
    cedulas = 0