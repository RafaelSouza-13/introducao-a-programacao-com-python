valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario: '))
anos = int(input('Digite em quantos anos deseja pagar a casa: '))

fatura_mensal = (salario * 30) / 100
meses = anos * 12
prestacao_mensal = valor / meses

if(prestacao_mensal > fatura_mensal):
  print('Não é possivel o emprestimo bancário')
else:
  print('Emprestimo aprovado')
