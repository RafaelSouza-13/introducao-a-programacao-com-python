l = [15, 7, 27, 39]
n = int(input('Digite um valor a procurar: '))
m = int(input('Digite um segundo valor a procurar: '))
i = 0
while(i < len(l)):
  if(l[i] == n or l[i] == m):
    break
  i += 1
if(i == len(l)):
  print(f'Valor {n} e {m} não encontrados na lista')
elif(l[i] == n):
  print(f'Valor {n} encontrado primeiro na posicao {i}')
else:
  print(f'Valor {m} encontrado primeiro na posicao {i}')
  