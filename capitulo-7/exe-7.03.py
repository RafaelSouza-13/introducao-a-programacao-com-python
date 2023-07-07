palavra_1 = 'CTA'
palavra_2 = 'ABCX'
palavra_3 = palavra_1 + palavra_2
lista = []

for letra in palavra_3:
  if letra not in palavra_1 or letra not in palavra_2:
    lista.append(letra)
lista = "".join(lista)
print(lista)