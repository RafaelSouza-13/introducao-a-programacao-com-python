quantidade = int(input('Quantidade de cigarros fumado por dia: '))
anos = int(input('Quantos anos fumando: '))

perda = (10 * quantidade) * (anos * 365)
dias_perdidos = ((perda / 60) / 24)

print(f'A quantidade de dias perdidos: {dias_perdidos:.2f}')
