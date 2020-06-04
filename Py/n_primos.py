op="S"
while op=="S" or op=="s":
    numero = int(input("Digite um valor: "))
    cont=0
    aux = 1
    while aux<=numero:
        if numero%aux==0:
            cont+=1
        aux+=1
        
    if cont>2:
        print("valor nao é primo")
    else:
        print("valor primo")
    op=str(input("Desejas continuar(S ou N): "))
