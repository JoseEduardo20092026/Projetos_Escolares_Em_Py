
#Algoritmo que pergunta ao usuario quantos números gostária de digitar e mostre ao usuario quais números são pares e quais são impares. Usando a estrutura de repetição while

Resposta_Do_Usuario=int(input("Quantos números gostária de digitar?"))
Contador=0
Lista_De_Numeros_Pares=[]
Lista_Dos_Numeros_Impares=[]
while Contador<Resposta_Do_Usuario:
    Numero_Digitado_Pelo_Usuario=float(input("Digite um número"))
    if Numero_Digitado_Pelo_Usuario%2==0:
        Lista_De_Numeros_Pares.append(Numero_Digitado_Pelo_Usuario)
    elif Numero_Digitado_Pelo_Usuario%2==1:
        Lista_Dos_Numeros_Impares.append(Numero_Digitado_Pelo_Usuario)
    Contador+=1
print(Lista_De_Numeros_Pares,"São valoes pares")
print(Lista_Dos_Numeros_Impares,"São valores impares")