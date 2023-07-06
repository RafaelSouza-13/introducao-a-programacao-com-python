l = [15, 7, 27, 39]
n = int(input('Digite um valor a procurar: '))
i = 0
while(i < len(l)):
  if(l[i] == n):
    break
  i += 1
if(i == len(l)):
  print(f'Valor {n} não encontrado na lista')
else:
  print(f'Valor {n} encontrado na posicao {i}')
