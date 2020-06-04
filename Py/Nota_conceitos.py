Nome = str (input("Digite seu Nome :"))
sexo = str(input("Insira seu sexo (M ou F) :"))

Nota1 = float (input("Digite a nota 1 :"))
Nota2 = float (input("Digite a nota 2 :"))
Nota3 = float (input("Digite a nota 3 :"))

media_aluno=(Nota1+Nota2+Nota3)/3

if sexo == "M" or sexo =="m":
              print("Aluno : ", Nome)
              
elif sexo == "F" or sexo =="f":
              print("Aluna : ", Nome)
              
if media_aluno <= 4.9:
              print ("conceito =  ( I )")
elif media_aluno >4.9 and media_aluno <= 6.9:
              print ("conceito =  ( R )")
elif media_aluno > 6.9 and media_aluno <= 8.9:
              print ("conceito =  ( B )")
else:
             print ("conceito =  ( E )")


