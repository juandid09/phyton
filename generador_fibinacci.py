#serie fibonacci
#0 1 1 2 3 4 5 13 21 ..

def fibonacci(limite):
    a, b = 0 , 1
    #a = 0
    #b = 1 
    # a es 0 y b es 1
    while a < limite: 
        yield a

        
        # Guardamos el valor de `a` en una variable temporal
        nuevo_a = b
        # Calculamos el nuevo valor de `b`
        nuevo_b = a + b
        
        # Asignamos los valores a `a` y `b`
        a = nuevo_a
        b = nuevo_b

for num in fibonacci(10):
    print(num)

