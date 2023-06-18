n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
decrementador = n1
contador = 0
while(decrementador >= n2):
  decrementador -= n2
  contador += 1
  if(decrementador == n2):
    modulo = 0
  else:
    modulo = abs(decrementador)

if(modulo == 0):
  print(f'Divisão inteira entre {n1} / {n2} = {contador}')    
else:
  print(f'Divisão inteira entre {n1} / {n2} = {contador}, com resto {modulo}')
