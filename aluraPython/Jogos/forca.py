from random import randrange

def imprime_mensagem_abertura():
    print("**************************")
    print("Bem vindo ao jogo da Forca")
    print("**************************")
    
def carrega_palavra_secreta():
    arquivo = open("palavra.txt","r")
    palavras= []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    
    num = randrange(0,len(palavras))
    return palavras[num].upper()
    
def inicializa_letras_acertadas(palavra):
    return ["_" for i in palavra]

def jogar():
    imprime_mensagem_abertura()    
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    pontos = 0
    tentativas = 6
    quant = len(palavra_secreta)
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0   
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    pontos += 1
                index += 1
            print(f"Você ainda tem {tentativas} chances")
        else:
            print(f"Você ainda tem {tentativas} chances")
            tentativas -= 1
        
        print(letras_acertadas)
        
        if(pontos >= quant):
            acertou = True
            
        enforcou = tentativas == 0
    
    if(acertou):
        print(f"Parabéns você ganhou!!")
        print(f"Você ficou com {pontos} pontos ")
    else:
        print(f"Que pena, você não acertou! A palavra secreta era {palavra_secreta.capitalize()}")
        
    print("Fim do jogo")
    

if(__name__=="__main__"):
    jogar();