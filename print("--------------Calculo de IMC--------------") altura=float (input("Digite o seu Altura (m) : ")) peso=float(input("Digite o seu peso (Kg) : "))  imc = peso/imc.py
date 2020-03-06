print("--------------Calculo de IMC--------------")
altura=float (input("Digite o seu Altura (m) : "))
peso=float(input("Digite o seu peso (Kg) : "))

imc = peso/(altura*altura)

if imc < 18.5:
              imc= round(imc,2)
              print("\nIMC =", "%.2f" %imc, "\nabaixo do peso")
elif imc>18.4 and imc<25:
              print("\nIMC =", "%.2f" %imc, "\npeso normal")
elif imc>24.9 and imc<30:
              print("\nIMC =", "%.2f" %imc, "\nsobrepeso")
elif imc>29.9 and imc<35:
              print("\nIMC =", "%.2f" %imc, "\nobesidade grau I")
elif imc>34.9 and imc<40:
              print("\nIMC =", "%.2f" %imc, "\nobesidade grau II")
else:
              print("\nIMC =", "%.2f" %imc, "\nobesidade grau III")
