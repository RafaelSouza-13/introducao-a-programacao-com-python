n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
multiplicacao = 0
i = 0

while(i < n2):
  multiplicacao += n1
  i += 1
  
print(f'{n1} * {n2} = {multiplicacao}')