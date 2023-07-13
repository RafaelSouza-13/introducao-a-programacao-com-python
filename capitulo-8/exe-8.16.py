def imprimir_lista(lista, nivel=0):
  espacamento = "\t" * nivel
  for elemento in lista:
    if type(elemento) is int:
      print(espacamento, end="")
      print(f'{elemento}')
      continue
    else:
      print(espacamento+'{')
      imprimir_lista(elemento, nivel + 1)
      print(espacamento+'}')

l = [1, [2, 3, 4, [5, 6, 7]]]
imprimir_lista(l)
