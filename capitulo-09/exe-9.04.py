import sys

if(len(sys.argv) != 3):
  pass
else:
  primeiro_arquivo = sys.argv[1]
  segundo_arquivo = sys.argv[2]
  with open('resultado-9.4.txt', 'w') as r, open(primeiro_arquivo, 'r') as p, open(segundo_arquivo, 'r') as s:
    for i in p.readlines():
      r.write(f'{i}')
    r.write("\n")
    for i in s.readlines():
      r.write(f'{i}')
    