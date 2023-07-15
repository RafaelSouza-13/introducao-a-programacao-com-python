def gerador_primos():
  i = 2
  while(True):
    if(i == 2 or i == 3):
      yield i
    elif((i > 5 and i % 5 == 0) or (i > 7 and i % 7 == 0)):
      i += 1
      continue
    elif((i % 2 != 0 and i % 3 != 0)):
      yield i
    i += 1

# g = gerador_primos()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
primos = []
g = gerador_primos()
try:
  n = int(input('Digite a quantidade de numeros primos de deseja: '))
except ValueError:
  print('Valor invalido')
else:
  for i in range(n):
    primos.append(next(g))
finally:
  print(primos)
  print('Encerrando o programa')
