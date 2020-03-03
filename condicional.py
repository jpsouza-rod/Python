# Receba dois valores que correspondam a idade de duias crianças, mostre na tela quem é o mais velho e a diferença de idade
idade1 = int (input("Digite a idade da criança 1 :"))
idade2 = int (input("Digite a idade da criança 2 :"))

if idade1<idade2:
              print("crianca 2 é a mais velha com ", idade2-idade1, " anos de diferença")
else:
              print("crianca 1 é a mais velha com ", idade1-idade2, " anos de diferença")

