numero_1 = 0
numero_2 = 0
operacao = 0
operacao1 = 1
operacao2 = 2
operacao3 = 3
operacao4 = 4
# Aqui vamos dar para o usuario decidir qual operação ele deseja efetuar.
operacao = int(input("Digite a operacao desejada (1 para soma, 2 para sub, 3 para mult, 4 para div): "))
if operacao1 == 1:
    print("vamos começar as operações de adição")
elif operacao2 == 2:
    print("vamos começar as operações de subtração")
elif operacao3 == 3: 
    print("vamos começar as operações de multiplicação")
elif operacao4 == 4:
    print("vamos começar as operações de dividir")
else: 
    print("opção invalida")


numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

if operacao == "soma":
	resultado = int(numero1) + int(numero2)
if operacao == "sub":
	resultado = int(numero1) - int(numero2)
if operacao == "mult":
	resultado = int(numero1) * int(numero2)
if operacao == "div":
	resultado = int(numero1) / int(numero2)
else:
	resultado = "Operação não suportada"
    
print("O resultado da operação é: " + str(resultado))