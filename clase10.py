#diccionarios 

num = {1:"uno",
       2:"dos",
       3:"tres"}

print(num[2]) #con la llave busco el valor 

inf = {"nombre":"wilson",
       "edad":1.6,
       "color":"blanco"}

print(inf) 

del inf["color"]

print(inf) 

#saber las claves
claves = inf.keys()
print("claves:", claves)

#saber valores
values = inf.values()
print("claves:", values)

#diccionarios de diccionarios ejemplo agenda 

agenda = {"PERRRITO":{"nombre":"wilson",
          "edad":1.6,
          "color":"blanco"},

          "GATITO":{"nombre":"pereza",
          "edad":1.9,
          "color":"blanco negro"}}

print(agenda["PERRRITO"])