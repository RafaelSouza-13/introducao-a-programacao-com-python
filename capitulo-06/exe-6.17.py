estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijao": [100, 1.50]}

vendas = []
while True:
  nome = input('Digite o nome do produto ("fim" para sair): ').lower()
  if nome == 'fim':
    break
  quantidade = int(input('Digite a quantidade: '))
  elementos = [nome, quantidade]
  vendas.append(elementos)
  
total = 0
print('Vendas: \n')
for venda in vendas:
  produto = venda[0]
  quantidade = venda[1]
  if produto in estoque:
    preco = estoque[produto][1]
    custo = quantidade * preco
    print(f'{produto}: {quantidade} x {preco:.2f} = {custo:.2f}')
    estoque[produto][0] -= quantidade
    total += custo
  else:
    print('Porduto nao encontrado')
print('\n\n')
print(f'Custo total: {total:.2f}')
print('Estoque: \n')
for chave, valor in estoque.items():
  print(f'Descricao: {chave}')
  print(f'Quantidade: {valor[0]}')
  print(f'Preco: {valor[1]:.2f}')
  print(f'\n')