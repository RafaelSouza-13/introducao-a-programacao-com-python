import random

def le_numero(arquivo):
  while True:
    numero = arquivo.readline()
    if numero == "":
      return None
    if numero.strip() != "":
      return int(numero)
    
def escreve_numero(arquivo, n):
  arquivo.write(f"{n}\n")

tamanho_lista = 50
inicio = 1
fim = 1000
lista = list(range(inicio, fim + 1))
sorteados = random.sample(lista, tamanho_lista)
sorteados.sort()

with open('pares.txt', 'w') as par, open('impares.txt', 'w') as impar:
  for i in sorteados:
    if i % 2 == 0:
      par.write(f'{i}\n')
    else:
      impar.write(f'{i}\n')

with open('pares.txt', 'r') as pares, open('impares.txt', 'r') as impares, open('pares_impares.txt', 'w') as pares_impares:
  npar = le_numero(pares)
  nimpar = le_numero(impares)
  while True:
    if npar is None and nimpar is None: 
        break
    if npar is not None and (nimpar is None or npar <= nimpar):
        escreve_numero(pares_impares, npar)
        npar = le_numero(pares)
    if nimpar is not None and (npar is None or nimpar <= npar):
        escreve_numero(pares_impares, nimpar)
        nimpar = le_numero(impares)