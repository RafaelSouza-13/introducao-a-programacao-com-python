palavra_1 = 'AATTCGAA'
palavra_2 = 'TG'
palavra_3 = 'AC'
resultado = palavra_1[:]
x = 0
while(x < len(palavra_2)):
  if palavra_2[x] in resultado:
    resultado = resultado.replace(palavra_2[x], palavra_3[x])
  x += 1

print(resultado)