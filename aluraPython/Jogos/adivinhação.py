from random import randint, random, randrange, seed

def jogar():
    numero_secreto = randint(1,100);
    tentativas = 0;
    
    print("escolha o nível de dificuldade: ")
    nivel = int(input("(1) fácil (2) médio (3) dificil: "))
    if(nivel < 1 or nivel > 3):
        print("ERRO!! nível inválido!! por favor digite o nível novamente")
        nivel = int(input("(1) fácil (2) médio (3) dificil: "))
        
    if(nivel == 1):
        tentativas = 20;
    elif(nivel == 2):
        tentativas = 10;
    else:
        tentativas = 5;



    for i in range(1,tentativas+1):
        chute = input("Digite o seu número: ");
        if(int(chute) == -1):
            break;

        if(numero_secreto == int(chute)):
            print("você acertou");
            break;
        elif(numero_secreto > int(chute)) :
            print("O numero digitado é menor q o número secreto");
        else:
            print("O número digitado é maior que o número secreto");

        if(i == tentativas):
            print(numero_secreto);

if(__name__=="__main__"):
    jogar()