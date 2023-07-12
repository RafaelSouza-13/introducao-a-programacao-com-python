def procura(lista, nome):
  if nome in lista:
    return True
  return False
drinks = ['caipirinha', 'margarita', 'mojito', 'manhattan', 'sex on the beach', 'negroni', 'cuba libre']

drink = input('Digite o nome de um drink: ').lower()
resultado = procura(drinks, drink)
print(resultado)
