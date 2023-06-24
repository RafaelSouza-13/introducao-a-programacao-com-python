palavra = input('Digite um texto sem espaços: ')
palavra = palavra.strip(" ").lower()
tamanho_palavra = len(palavra)
inicio = 0
fim = tamanho_palavra -1
while inicio != fim and palavra[inicio] == palavra[fim]:
  inicio += 1
  fim -= 1
if palavra[inicio] == palavra[fim]:
  print(f'O texto {palavra} é um palindromo')
else:
  print(f'O texto {palavra} não é um palindromo')
  