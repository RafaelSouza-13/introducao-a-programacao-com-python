temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]
max = temperaturas[0]
min = temperaturas[0]

for temperatura in temperaturas:
  if max < temperatura:
    max = temperatura
  if min > temperatura:
    min = temperatura

media_temperatura = sum(temperaturas) / len(temperaturas)
print(f'Menor temperaura registrada: {min} \nMaior temperatura registrada: {max} \nMedia as temperaturas: {media_temperatura}')
