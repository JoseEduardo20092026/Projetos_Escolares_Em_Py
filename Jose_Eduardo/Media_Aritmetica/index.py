
#Algiritmo que receba o número de notas e calcule a media entre eles e mostre
#Media maior que 6 mostrar aprovado,maior ou igual  a 4 e menor que 6 mostrar
#recuperação e menor que 4 mostrar reprovado

Resposta_Do_Usuario=int(input("Digite quantas notas gostária de digitar : "))
Notes_List=[]
Soma_Das_Notas=0
Media_Das_Notas=0
for A in range(Resposta_Do_Usuario):
    Notas=float(input("Digite sua nota: "))
    Soma_Das_Notas+=Notas
    Media_Das_Notas=Soma_Das_Notas/Resposta_Do_Usuario
print("A media das notas digitadas é igual a:",Media_Das_Notas)    
Aprovado=[]
Recuperacao=[]
Reprovado=[]
if Media_Das_Notas>=6.0:
    Aprovado.append(Media_Das_Notas)
    print("Aprovado")
elif Media_Das_Notas>=4.0 and Media_Das_Notas<6.0:
    Recuperacao.append(Media_Das_Notas)
    print("Recuperação")
elif Media_Das_Notas<4.0 and Media_Das_Notas>=0:
    Reprovado.append(Media_Das_Notas)
    print("Reprovado")
        



