import sys

if len(sys.argv) != 2: 
    print("Tente: exe-9.01.py nome.txt\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():
        print(linha[:-1])
    arquivo.close()