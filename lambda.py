add = lambda a,b : a+b

print(add(10,4))

multiplicacion = lambda a,b :a*b
print(multiplicacion(10,4))

#tener el cuadrado de cada numero 

numeros = range(11)

numeros_cuadrados = list(map(lambda X: X**2,numeros))

print("cuadrados:", numeros_cuadrados)


#numeros pares 
#el ultimo es a donde se quiere aplicar 
numeros_pares = list(filter(lambda X: X%2==0,numeros))
print("pares:", numeros_pares)