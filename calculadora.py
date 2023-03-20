numero_1 = 0
numero_2 = 0
operacao = 0
resultado = ""

while operacao != "s": # Aqui o usuario vai decidir se deseja faser outra operação ou não.

# Aqui vamos dar para o usuario decidir qual operação ele deseja efetuar.
    operacao = int(input("Digite a operacao desejada (1 para soma, 2 para sub, 3 para mult, 4 para div): "))
    if operacao == 1:
        print("vamos começar as operações de adição")
        numero_1 = input("Digite o primeiro número: ")
        numero_2 = input("Digite o segundo número: ")
        resultado= float(numero_1) + float(numero_2)
# cada bloco de if ja tem as operações a serem feita. 
    elif operacao == 2:
        print("vamos começar as operações de subtração")
        numero_1 = input("Digite o primeiro número: ")
        numero_2 = input("Digite o segundo número: ")
        resultado= float(numero_1) - float(numero_2)
    elif operacao == 3: 
        print("vamos começar as operações de multiplicação")
        numero_1 = input("Digite o primeiro número: ")
        numero_2 = input("Digite o segundo número: ")
        resultado= float(numero_1) * float(numero_2)
    elif operacao == 4:
        print("vamos começar as operações de dividir")
        numero_1 = input("Digite o primeiro número: ")
        numero_2 = input("Digite o segundo número: ")
        resultado= float(numero_1) / float(numero_2)
    else: 
        print("opção invalida")

    print("O resultado da operação é: " + str(resultado))

    operacao = input("Digite [s] para sair o [c] para continuar: ")