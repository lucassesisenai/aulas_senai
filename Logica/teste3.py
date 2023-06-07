
n1 = int(input("Digite o 1° nota:"))
n2 = int(input("Digite o 2° nota:"))
n3 = int(input("Digite o 3° nota:"))
n4 = int(input("Digite o 4° nota:"))
n5 = int(input("Digite o 5° nota:"))

nota1 = (n1+n2+n3)/3
nota2 = (n4+n5)/2

resultado = (nota1 + nota2)/2

print("Sua nota é:", resultado)


if(resultado >= 7 ):
    print("Aluno está Aprovado!") 
elif(resultado < 7) and (resultado >=5):
     print("Aluno está de Conselho!") 
else:
      print("Aluno está Reprovado!")     
