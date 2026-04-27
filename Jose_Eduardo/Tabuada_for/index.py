
#Algoritmo que pergunte ao usuario de qual número ele gostária de ver a tabuada.
#Depois de digitado, parguntar ao usuario qual a operação ele deseja escolher: soma,subtração multiplicação ou divisão.

Resposta_Do_Usuario=int(input("De qual número você gostaria de ver a tabuada?"))
Opicoes=int(input("1-Soma 2-Subtração 3-Multiplicaçao 4-Divisão "))
Tabuada=0
if(Opicoes==1):
    for A in range(10):
        Tabuada=A+Resposta_Do_Usuario
        print(Tabuada)
elif(Opicoes==2):
    for B in range(10):
        Tabuada=Resposta_Do_Usuario-B
        print(Tabuada)
elif(Opicoes==3):
    for C in range(10):
        Tabuada=C*Resposta_Do_Usuario
        print(Tabuada)
elif(Opicoes==4):
    for D in range(10):
        Tabuada=D/Resposta_Do_Usuario
        print(Tabuada)        
