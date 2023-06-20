valor_total = 0
while(True):
  print('Codigo: 1 - Preço: 0,50 R$ \n Codigo: 2 - Preço: 1,00 R$ \n Codigo: 3 - Preço: 4,00 R$ \n Codigo: 5 - Preço: 7,00 R$ \n Codigo: 9 - Preço: 8,00 R$ \n Codigo: 0 - Sair')
  codigo = input('Digite um codigo: ')
  if(codigo == '0'):
    print('Operação encerrada')
    break
  quantidade_produto = input('Digite a quantidade do produto: ')
  try:
    quantidade_produto = int(quantidade_produto)
  except ValueError:
    print('Valor da quantidade inválido!')
    continue
  if(codigo == '1'):
    valor_total += quantidade_produto * 0.5  
  elif(codigo == '2'):
    valor_total += quantidade_produto * 1
  elif(codigo == '3'):
    valor_total += quantidade_produto * 4
  elif(codigo == '5'):
    valor_total += quantidade_produto * 7
  elif(codigo == '9'):
    valor_total += quantidade_produto * 8
  else:
    print('Codigo inválido')
      
print(f'Total das compras: {valor_total}')