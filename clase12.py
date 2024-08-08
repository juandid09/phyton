num = [1,2,3,4,5,6]

for i in num: 
    print("el valor es:", i+1) 

for i in range(10):
    print("el valor es:",i)

for i in range(3,10):
    print("el valor es:",i)

frutas = ["manzana","mango","uva","tomate"]

for fruta in frutas:
    print(fruta)
    if fruta == "uva":
        print("uvita encontrada")

x = 0
while x < 5:
    if x == 3:
        break #terminar 
    print(x)
    x = x+1

num = [1,2,3,4,5,6]

for i in num: 
    if i ==3:
        continue #continuar
    print("el valor es:", i) 