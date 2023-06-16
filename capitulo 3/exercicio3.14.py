qp = int(input('Quantidade de kilometros percorrida: '))
dias = int(input('Quantidade de dias alugado: '))
preco = (60 * dias) + (qp * 0.15)

print(f'Total a pagar: {preco:.2f}')