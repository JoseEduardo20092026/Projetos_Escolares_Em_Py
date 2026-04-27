Resposta_Do_Usuario=int(input("Quantos números gostaria de digitar?"))
Contador=0
Soma_Dos_Numeros=0
Media_Dos_Numeros=0
while Contador<Resposta_Do_Usuario:
    Numero_Digitado_Pelo_Usuario=float(input("Digite um número"))
    Soma_Dos_Numeros+=Numero_Digitado_Pelo_Usuario
    Media_Dos_Numeros=Soma_Dos_Numeros/Resposta_Do_Usuario
    Contador+=1
print("Asoma dos valores digitados é igual á: ",Soma_Dos_Numeros)
print("A media dos valores digitados é igual á: ",Media_Dos_Numeros)