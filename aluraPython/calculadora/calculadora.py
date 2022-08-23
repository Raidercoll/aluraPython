conta = True
while(conta == True):
    print("Bem vindo a calculadora")

    print("digite:",  end = "\n")
    print("(1) subtração, (2) multiplicação, (3) soma , (4) divisão, (5) sair")
    num = int(input())
    if(num > 5):
        print("Função inválida")
        break;
    num1 = int(input("Digite o primeiro número "))
    num2 = int(input("Digite o segundo número "))

    if(num == 1):
        print(num1 - num2)
    elif(num ==2):
        print(num1 * num2)
    elif(num == 3):
        print(num1 + num2)
    elif( num == 4):
        print(num1 / num2)
    elif(num == 5):
        print("Obrigado por usar a calculadora")
        break;