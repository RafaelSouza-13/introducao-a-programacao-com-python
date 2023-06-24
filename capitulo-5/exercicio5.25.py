numero = float(input("Digite um número para encontrar a raiz quadrada: "))
base = 2
if numero == 4.0:
  p = 2
while abs(numero - (base * base)) > 0.00001:
    p = (base + (numero / base)) / 2
    base = p
print(f"A raiz quadrada de {numero} é aproximadamente: {p:.4f}")