dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
x = dividendo
while x >= divisor:
    x -= divisor
resto = x
print(f"Resto da divisão de: {dividendo} / {divisor} = {resto}")