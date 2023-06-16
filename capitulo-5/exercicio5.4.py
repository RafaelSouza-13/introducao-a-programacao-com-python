ultimo = int(input('Digite o ultimo numero a imprimir: '))
contador = 1

while(contador <= ultimo):
  if(contador % 2 != 0):
    print(contador)
  contador += 1