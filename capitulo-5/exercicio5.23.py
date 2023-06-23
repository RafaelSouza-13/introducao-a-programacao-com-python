numero = int(input("Digite um número: "))
if numero < 0:
    print("Número inválido! o número de entrada deve ser positivo")
if numero == 0 or numero == 1:
    print(f"{numero} não tem numeros primos.")
else:
    if numero == 2:
        print("2 é primo")
    elif numero % 2 == 0:
        print(f"O {numero} não pode ser primo pois 2 é o único número par primo.")
    else:
        divisor = 3
        while(divisor < numero):
            if numero % divisor == 0:
                break
            divisor += 2
        if divisor == numero:
            print(f"O numero {numero} é primo")
        else:
            print(f"O numero {numero} não é primo pois é divisível por {divisor}")