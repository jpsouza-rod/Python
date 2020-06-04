num = 1000
cont=0
i=0

while num>=1000 and num<=2000:
    if num%2 == 0:
        cont+=1
    num+=1
print ("O numero de numeros pares é ", cont)

for i in range(10): #for i=0; i<n; i++
    print("n :", i+1)

cont=0

for i in range (201,1001,2):  #for i=0; i<n; i++
    if i%2==1:
        cont+=1
print(cont)
    

