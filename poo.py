class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self): 
        print(f"mi nombre es: {self.nombre} y la edad es: {self.edad}")

pesona1 = Persona("wilson",12)
pesona2 = Persona("Kiara",15)

pesona1.saludar()
pesona2.saludar()