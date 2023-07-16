def cria_lista(arquivo):
  lista = []
  for a in arquivo:
    lista.append(a)
  lista.reverse()
  return lista

with open('pares.txt', 'r') as p:
  lista = cria_lista(p)

with open('inverte_pares.txt', 'w') as i:
  for l in lista:
    i.write(f'{l}')