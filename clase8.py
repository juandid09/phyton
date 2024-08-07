#listas 
to_do = ["ir al hotel",
         "almorzar",
         "pasear al perro",
         "correr"]

print(to_do)

num = [1,2,3,4,"cinco"]

print(num)
print(type(num))

#lista
mix = ["uno", 2, 3.14, True , [1,2,3]]
print(mix)
print(len(mix))
print("primer elemento:", mix[0])

print("resul: ",mix[0:2]) #quiero optener desde cero al elemento 2 si lo dejo vasio va desde el inicio hasta el final [:]

#cadena
string = "hola wilson"
print(string)
print(len(string))
print("primer elemento:", string[0])

#añadir elemento a la lista 
print(mix)
mix.append(False) #añado elemento a la ultima lista 

print("elemento sumado:",mix)

#insertar un dato 
mix.insert(1,["a","b"])
print("elemento insertado en la posicion 1:",mix)

#conocer la posicion del elemento del primero que encuentre en caso que se repita
print("la posicion es:",mix.index("uno"))

#conocer el dato mayor de la lista 
lista_num = [1,2,3,9,100,7]
print("El numero mayor es:", max(lista_num))

#conocer el dato menor de la lista 
lista_num = [1,2,3,9,100,7]
print("El numero menor es:", min(lista_num))

#eliminar datos de la lista
lista_num = [1,2,3,9,100,7]
del lista_num[1]
print(lista_num)

#eliminar datos de la lista por porsion
lista_num = [1,2,3,9,100,7]
del lista_num[0:1]
print(lista_num)

#eliminar toda la lista
lista_num = [1,2,3,9,100,7]
del lista_num
print(lista_num) #ejecuta error al correr porque no existe la lista 