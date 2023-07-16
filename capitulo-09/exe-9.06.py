LARGURA = 79
with open('entrada.txt') as entrada:
  for linha in entrada.readlines():
    if linha[0] == ';':
      continue
    elif linha[0] == '>':
      print(linha[1:].rjust(LARGURA))
    elif linha[0] == '*':
      print(linha[1:].center(LARGURA))
    elif linha[0] == '=':
      for i in range(1, 41):
        print('=',end=" ")
      print(linha[1:])
    elif linha[0] == '.':
      input("Precione enter para continuar a imprimir")
      print()
    else:
      print(linha)