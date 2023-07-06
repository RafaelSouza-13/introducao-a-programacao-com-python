notas = []
contador = 0
while contador < 7:
  valor = float(input(f'Digite a nota {contador + 1}: '))
  notas.append(valor)
  contador = len(notas)
somatorio = sum(notas)
media = round(somatorio / contador, 2)
print(f'Media do estudante: {media}')