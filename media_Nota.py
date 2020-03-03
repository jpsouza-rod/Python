
Nota1 = float (input("Digite a primeira nota :"))

Nota2 = float (input("Digite a segunda nota :"))

Nota3 = float (input("Digite a terceira nota :"))

Nota4 = float (input("Digite a quarta nota :"))

notaTotal= Nota1+Nota2+Nota3+Nota4
media = notaTotal/4

if media > 5:
              print("Aluno foi aprovado, a media foi igual a ", media)
else:
              print("Aluno foi reprovado, a media foi igual a ", media)
