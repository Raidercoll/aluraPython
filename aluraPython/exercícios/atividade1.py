num = int(input("Digite um número\n"))
this = True;
while(this == True ):
    resp = input("Deseja saber o sucessor e antecessor do número digitado?\n")
    if(resp.lower() == "sim"):
        print(f"Antecessor {num-1}")
        print(f"sucessor: {num+1}")
    else:
        print("Saindo...")
        this = False