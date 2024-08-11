def generador():

    yield 1
    yield 2
    yield 3
    yield 4

for valor in generador():
    print(valor)
      