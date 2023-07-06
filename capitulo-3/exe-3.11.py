preco = input('Digite o preço da mercadoria: ')
preco = float(preco)
percentual = input('Digite o percentual de desconto: ')
percentual = float(percentual)

desconto = (preco * percentual) / 100

print(f'O preço do produto é: {preco:.2f}, valor de desconto: {desconto:.2f} o valor fica: {preco - desconto} ')
