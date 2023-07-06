while True:
    print("1 - Adição \n2 - Subtração \n3 - Divisão \n4 - Multiplicação \n5 - Sair")
    opcao = int(input("Digite uma opção: "))
    if opcao == 5:
        break
    elif opcao >= 1 and opcao < 5:
        numero = int(input("Digite a tabuada de um número: "))
        x = 1
        while x <= 10:
            if opcao == 1:
                print(f"{numero} + {x} = {numero + x}")
            elif opcao == 2:
                print(f"{numero} - {x} = {numero - x}")
            elif opcao == 3:
                print(f"{numero} / {x} = {numero / x:5.4f}")
            elif opcao == 4:
                print(f"{numero} x {x} = {numero * x}")
            x = x + 1
    else:
        print("Opção inválida!")