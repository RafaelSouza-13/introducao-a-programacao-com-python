l = [15, 7, 27, 39]
n = int(input('Digite um valor a procurar: '))
m = int(input('Digite um segundo valor a procurar: '))
i = 0
acertos = 0
index_n = None
index_m = None
while(i < len(l)):
  if(l[i] == n or l[i] == m):
    if(l[i] == n):
      index_n = i
    else:
      index_m = i
    acertos += 1
  i += 1
  if(acertos == 2):
    break

if(acertos == 2):
  print(f'Valor {n} foi encontrado na posicao {index_n} e o valor {m} foi encontrado na posicao {index_m}')
elif(acertos == 1):
  if(index_n):
    print(f'O valor de {n} foi encontrado na posicao {index_n} e o valor {m} não foi encontrado na lista')
  else:
    print(f'O valor de {m} foi encontrado na posicao {index_m} e o valor {n} não foi encontrado na lista')   
else:
  print(f'Valor {n} e {m} não foram encontrados na lista')