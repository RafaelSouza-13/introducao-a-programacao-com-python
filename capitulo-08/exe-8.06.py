def soma(lista):
  total = 0
  for numero in lista:
    total += numero
  return total

lista = [1, 7, 2, 9, 15]
print(soma(lista))
print(soma([7, 9, 12, 3, 100, 20, 4]))
