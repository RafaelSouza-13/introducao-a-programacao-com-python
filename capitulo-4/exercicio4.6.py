distancia = int(input('Digite a distancia que deseja percorrer(km): '))

if(distancia <= 200):
  passagem = round(distancia * 0.5, 2)
else:
  passagem = round(distancia * 0.45, 2)

print(f'Valor da passagem: {passagem:.2f} R$')