numero_1 = 0
numero_2 = 0
operacao = 0

# Aqui vamos dar para o usuario decidir qual operação ele deseja efetuar.
operacao = int(input("Digite a operacao desejada (1 para soma, 2 para sub, 3 para mult, 4 para div): "))
if operacao == 1:
    print("vamos começar as operações de adição")
elif operacao == 2:
    print("vamos começar as operações de subtração")
elif operacao == 3: 
    print("vamos começar as operações de multiplicação")
elif operacao == 4:
    print("vamos começar as operações de dividir")
else: 
    print("opção invalida")


numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")


    
print("O resultado da operação é: " + str(resultado))