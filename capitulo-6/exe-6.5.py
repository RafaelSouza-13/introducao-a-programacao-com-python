ultimo = 10
fila = list(range(1,ultimo + 1))

while True:
  print(f'Existem {len(fila)} pessoas na fila')
  print(f'Fila atual: {fila}')
  print(f'Digite F para adicionar um cliente ao final da fila')
  print(f'ou A para realizar o atendimento. S para sair')
  operacao = input("Operacao: (A, F ou S):").lower()
  i = 0
  encerrar = False
  while(i < len(operacao)):
    if operacao[i] == 'a':
      if(len(fila) == 0):
        print('A fila esta vazia')
      else:
        atendimento = fila.pop(0)
        print(f'Cliente {atendimento} atendido')
    elif operacao[i] == 'f':
      ultimo += 1
      fila.append(ultimo)
      print(f'Cliente {ultimo} adicionado ao final da fila')
    elif operacao[i] == 's':
      print('Encerrando o programa')
      encerrar = True
      i += 1
      break
    else:
      print('Operacao invalida! digite apenas (A, F ou S)')
    i += 1
  if(operacao[i - 1] == 's'):
    break
  