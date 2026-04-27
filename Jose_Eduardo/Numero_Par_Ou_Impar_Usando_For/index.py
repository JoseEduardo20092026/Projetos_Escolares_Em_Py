
#Algoritmo que pergunta ao usuario quantos números gostária de digitar e mostre ao usuario quais números são pares e quais são impares. Usando a estrutura de repetição for

Resposta_Do_Usuario=int(input("Quantos números gostaria de digitar?"))
Lista_De_Numeros_Pares=[]
Lista_De_Numeros_Impares=[]
for A in range(Resposta_Do_Usuario):
    Numero_Digitado_Pelo_Usuario=float(input("Digite um número"))
    if Numero_Digitado_Pelo_Usuario%2==0:
        Lista_De_Numeros_Pares.append(Numero_Digitado_Pelo_Usuario)
    elif Numero_Digitado_Pelo_Usuario%2==1:
        Lista_De_Numeros_Impares.append(Numero_Digitado_Pelo_Usuario)
print(Lista_De_Numeros_Pares,"É par")
print(Lista_De_Numeros_Impares,"É impar")