def imprimir_lista(lista, nivel=0):
  espacamento = "\t" * nivel
  print(espacamento, end="")
  for elemento in lista:
    if type(elemento) is int:
      print(f'{elemento}', end=" ")
      continue
    else:
      print()
      nivel += 1
      imprimir_lista(elemento, nivel)

l = [1, [2, 3, 4, [5, 6, 7]]]
imprimir_lista(l)
