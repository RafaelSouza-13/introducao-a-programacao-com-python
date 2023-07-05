ultimo = 10
ultimo2 = 10
fila = list(range(1,ultimo + 1))
fila2 = list(range(1,ultimo2 + 1))

while True:
  print(f'Existem {len(fila)} pessoas na fila 1 e {len(fila2)} na fila 2')
  print(f'Fila 1 atual: {fila} \nfila 2 atual: {fila2}')
  print(f'Digite F para adicionar um cliente ao final da fila 1, digite G para o final da fila 2')
  print(f'ou A para realizar o atendimento da fila 1, digite para o atentimento da fila 2. S para sair')
  operacao = input("Operacao: (A, F ou S):").lower()
  i = 0
  encerrar = False
  while(i < len(operacao)):
    if operacao[i] == 'a':
      if(len(fila) == 0):
        print('A fila esta vazia')
      else:
        atendimento = fila.pop(0)
        print(f'Cliente {atendimento} da fila 1 foi atendido')
    elif operacao[i] == 'b':
      if(len(fila2) == 0):
        print('A fila esta vazia')
      else:
        atendimento = fila2.pop(0)
        print(f'Cliente {atendimento} da fila 2 foi atendido')
    elif operacao[i] == 'f':
      ultimo += 1
      fila.append(ultimo)
      print(f'Cliente {ultimo} adicionado ao final da fila 1')
    elif operacao[i] == 'g':
      ultimo2 += 1
      fila2.append(ultimo2)
      print(f'Cliente {ultimo2} adicionado ao final da fila 2')
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