lista_1 = []
lista_2 = []
while True:
  n = int(input('Digite numeros para a primeira lista: (0 - Sair): '))
  if(n == 0):
    break
  lista_1.append(n)
while True:
  m = int(input('Digite numeros para a segunda lista: (0 - Sair): '))
  if(m == 0):
    break
  lista_2.append(m)

lista_3 = []
lista_3 = lista_1.copy()
lista_3.extend(lista_2)
print(lista_3)
