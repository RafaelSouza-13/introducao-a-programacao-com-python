def pesquisa(lista, valor):
  if(valor in lista):
    return valor
  return None

l = [10, 20, 25, 30]
print(pesquisa(l, 25))
print(pesquisa(l, 27))