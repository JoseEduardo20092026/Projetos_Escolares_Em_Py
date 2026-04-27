
#Algoritmo que pergunta ao usuário quantos números gostária de digitar e mostrar ao usuário a soma dos valores digitados e a media deles

Resposta_Do_Usaurio=int(input("Quantos números gostaria de digitar?"))
Soma_Dos_Numeros=0
Media_Dos_Numeros=0
for A in range(Resposta_Do_Usaurio):
    Numero_Digitado_Pelo_Usuario=float(input("Digite um valor"))
    Soma_Dos_Numeros+=Numero_Digitado_Pelo_Usuario
    Media_Dos_Numeros=Soma_Dos_Numeros/Resposta_Do_Usaurio
print("A soma dos valores digitados é igual á: ",Soma_Dos_Numeros)
print("A media dos valores digitados é igual á: " , Media_Dos_Numeros)