a = [1,2,3,4,5]
b = a
print(a)
print(b)

del a [0]

print(id(a))
print(id(b)) #id conocer el espacio en memoria slice

c = a[:]
a.append(6)
print(id(c))

print(a)
print(c)
