palavra = 'TTAAC'
check = {}
p = 0
contador = 1
for letra in palavra:
  if letra not in check:
    quantidade = palavra.count(letra)
    print(f'{letra}: {quantidade}x')
    check[letra] = quantidade
  