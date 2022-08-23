
import adivinhação;
import forca;


    
print("**************************");
print("Qual jogo você quer jogar?");
print("**************************");

print("(1) Forca (2) adivinhação")
jogo = int(input("-->"));

if(jogo == 1):
    forca.jogar();
elif(jogo == 2):
    adivinhação.jogar();
else:
    print("ERRO!! Jogo não existente")