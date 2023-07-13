def gerador_fib():
  antecessor = 0
  sucessor = 1
  while(True):
    yield sucessor
    antecessor, sucessor = sucessor, sucessor + antecessor

fibonacci = []
fb = gerador_fib()
try:
  n = int(input('Digite a quantide de elementos sequencia fibonacci: '))
except ValueError:
  print('Valor invalido')
else:
  for i in range(n):
    fibonacci.append(next(fb))
finally:
  print(fibonacci)
  print('Encerrando o programa')