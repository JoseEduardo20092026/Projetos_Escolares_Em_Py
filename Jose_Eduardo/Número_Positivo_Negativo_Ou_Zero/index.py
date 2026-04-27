
#Algoritmo que leia uma quantidade de números inteiros digitado pelo usuário e mostre ao usuário se são negativo ou possitivo ou zero

Resposta_Do_Usuario = int(input("Quantos números você quer digitar? "))
Numeros=[]
for i in range(Resposta_Do_Usuario):
    Valor=int(input("Digite um número: "))
    Numeros.append(Valor)
Numeros_Positivos=[]
Numeros_Negativos=[]
Numero_Nulo=[]
for Valor in Numeros:
    if Valor>0:
        Numeros_Positivos.append(Valor)
    elif Valor<0:
        Numeros_Negativos.append(Valor)
    else:
        Numero_Nulo.append(Valor)    
print("Números pares:", Numeros_Positivos)
print("Números ímpares:", Numeros_Negativos)
print("Numeros nulos",Numero_Nulo)