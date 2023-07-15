lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = [1, 2, 30, 4, 50, 60, 7, 80, 9, 10]
sem_alteracao = set(lista_1) & set(lista_2)
novos_elementos = set(lista_2) - sem_alteracao
elementos_removidos = set(lista_1) - set(lista_2)

print(f'Elementos que nao sofreram alteracao: {sem_alteracao}')
print(f'Novos elementos: {novos_elementos}')
print(f'Elementos removidos: {elementos_removidos}')