somatorio = 0
tamanho = 0
while(True):
  valor = int(input('Digite um número inteiro: '))
  if(valor == 0):
    break
  somatorio += valor
  tamanho += 1

media = somatorio / tamanho
print(f'Quantidade de números digitados: {tamanho}, soma: {somatorio} e media: {media}')