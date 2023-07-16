import sys

nome = sys.argv[1]
inicio = int(sys.argv[2])
fim = int(sys.argv[3])
if len(sys.argv) != 4:
  print('Tente: python exe-9.02.py nome.txt 1 6')
else:
  with open(nome, 'r') as arquivo:
    for linha in arquivo.readlines()[inicio - 1: fim]:
      print(linha)