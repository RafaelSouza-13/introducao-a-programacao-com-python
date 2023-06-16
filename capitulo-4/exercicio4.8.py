n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

operacao = input('soma digite: + \n subtração digite: - \n multiplicação digite: * \n divisão digite: / \n operação: ')

if(operacao == '+'):
  print(f'{n1} + {n2}: {n1 + n2}')
elif(operacao == '-'):
  print(f'{n1} - {n2}: {n1 - n2}')
elif(operacao == '*'):
  print(f'{n1} x {n2}: {n1 * n2}')
elif(operacao == '/'):
  print(f'{n1} / {n2}: {n1 / n2}')
else:
  print('Operação invalida')