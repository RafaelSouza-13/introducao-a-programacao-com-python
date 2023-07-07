lista_1 = [1, 16, 20, 29, 3, 16, 19, 26, 29, 20, 28, 22, 22, 12]
lista_2 = [27, 14, 6, 29, 3, 1, 22, 30, 26, 18, 26, 20, 21, 21]
conjunto_1 = set(lista_1)
conjunto_2 = set(lista_2)
intersecao = conjunto_1 & conjunto_2
diferenca_1 = conjunto_1 - intersecao
diferenca_2 = conjunto_2 - intersecao
uniao = list(conjunto_1 | conjunto_2)
print(f'Lista 1: {lista_1}')
print(f'Lista 2: {lista_2}')
print(f'Valores em comum: {intersecao}')
print(f'Valores que so existem na primeira lista: {diferenca_1}')
print(f'Valores que so existem na segunda lista: {diferenca_2}')
print(f'Lista com elementos não repetidos das duas listas: {uniao}')