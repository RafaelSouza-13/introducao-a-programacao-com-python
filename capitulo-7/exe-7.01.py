palavra_1 = 'AABBEFAATT'
palavra_2 = 'BE'
posicao = palavra_1.find(palavra_2)
if posicao != -1:
  print(f'{palavra_2} encontrado na posicao {posicao} de {palavra_1}')
else:
  print(f'{palavra_2} nao encontrado')