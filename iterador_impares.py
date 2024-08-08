#crear interador para numero impares

#limite 

limite=10

#crear iterador
                #inicie en 1 con milite 10+1 y muevase 2 pociones 
iterador = iter(range(1,limite+1,2))

#usara iterador
for num in iterador:
    print(num)

#mismo ejercicio lista 

lista = [1]
nuevos_valores = []

for i in lista:
    if i < limite:
      lista.append(i+1)

# Añadir los nuevos valores a la lista original
#lista.extend(nuevos_valores)

for i in lista:
    print(i)

for i in lista:
    if i % 2 == 0:
        continue
    print("numeros son:",i)
