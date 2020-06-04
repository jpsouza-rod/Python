
input ("texto") #comando para pedir valor

#escreva um programa que pergunte a quantidade de quilometros pecorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos os quais o carros foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$ 0,15 por km rodado

kmRodado = float (input("digite quantos quilometros foram pecorridos: ")) 
qntDias = float (input("digite quantos dias o carro foi alugado: "))

valorTotal=kmRodado*0.15+qntDias*60

#para concatenar se usa ',' ou '+'
print("o valor total a pagar é R$",valorTotal)
