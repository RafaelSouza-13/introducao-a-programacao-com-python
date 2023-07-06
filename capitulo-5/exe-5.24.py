numero = int(input("Digite a quantidade de numeros primos de deseja: "))
if numero < 0:
    print("Número inválido! o número de entrada deve ser positivo")
else:
    if numero >= 1:
        print("Numeros primos: 2,", end=" ")
        contador = 1
        numeros_impar = 3
        while contador < numero:
            x = 3
            while(x < numeros_impar):
                if numeros_impar % x == 0:
                    break
                x += 2
            if x == numeros_impar:
                print(f'{x}, ', end=" ")
                contador += 1
            numeros_impar += 2