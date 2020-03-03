# Receba dois valores que correspondam a idade de duias crianças, mostre na tela quem é o mais velho e a diferença de idade
idade1 = int (input("Digite a idade da criança 1 :"))
idade2 = int (input("Digite a idade da criança 2 :"))

if idade1<idade2:
              print("crianca 2 é a mais velha com ", idade2-idade1, " anos de diferença")
else:
              print("crianca 1 é a mais velha com ", idade1-idade2, " anos de diferença")

if idade1 and idade2 >10:
              print("as duas crianças possuem idade superior a 10 anos")
    if idade1 or idade2 <20:
              print("umas das criancas possuem idade menor que 20 anos")
