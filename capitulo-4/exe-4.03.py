n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if(n1 >= n2):
  maior, menor = n1, n2
elif(n2 > n1):
  maior, menor = n2, n1
  
if(n3 > maior):
  maior = n3
elif(n3 < menor):
  menor = n3

if(maior != menor):
  print(f'O maior numero: {maior}, menor numero: {menor}')
else:
  print('Numero iguais')