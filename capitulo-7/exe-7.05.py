palavra_1 = 'AATTGGAA'
palavra_2 = 'TG'
palavra_3 = palavra_1[:]
for letra in palavra_2:
  if letra in palavra_1:
    palavra_3 = palavra_3.replace(letra, "")
print(palavra_3)