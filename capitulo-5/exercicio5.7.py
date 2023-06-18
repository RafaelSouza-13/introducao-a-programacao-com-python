numero = int(input('Digite o numero da tabuada: '))
inicio = int(input('Inicio da tabuada: '))
fim = int(input('Fim da tabuada: '))

if(inicio > fim):
  print('valor de inicio maior que o final!')
else:
  while(inicio <= fim):
    print(f'{inicio} x {numero} = {inicio * numero}')
    inicio += 1