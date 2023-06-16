salario = input('Digite o salário: ')
porcentagem = input('Digite a porcentagen do aumento: ')
salario = float(salario)
porcentagem = float(porcentagem)

novo_salario = salario + ((salario * porcentagem) / 100)

print(f'Salario antigo: {salario:.2f} sofreu um reajuste de {porcentagem:.2f}%. Novo salário: {novo_salario:.2f}')
