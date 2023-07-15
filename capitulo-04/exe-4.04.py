salario = float(input('Digite seu salario: '))

if(salario > 1250):
  novo_salario = salario + ((salario * 10) / 100)
else:
  novo_salario = salario + ((salario * 15) / 100)

print(f'Novo salario: {novo_salario}')
