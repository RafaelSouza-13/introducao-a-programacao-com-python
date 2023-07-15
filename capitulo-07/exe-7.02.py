palavra_1 = 'AAACTBF'
palavra_2 = 'CBTX'
palavra_3 = []

for letra in palavra_2:
  if letra in palavra_1:
    palavra_3.append(letra)
palavra_3 = "".join(palavra_3)
print(palavra_3)