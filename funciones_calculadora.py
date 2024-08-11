def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion (a,b):
    return a*b

def divicion (a,b):
    return a/b

def modulo (a,b):
    return a%b

def calculadora():
    while True:
          print("selecciones una opcion:")
          print("1.Suma")
          print("2.Resta")
          print("3.Multiplicacion")
          print("4.Divicion")
          print("5.Modulo")   
          print("6.SALIR")    

          opcion = input("Ingrese su opcion(1,2,3,4,5,6):")   
          
          if opcion == "6":
            print("saliendo de la calculadora")
            break

          if opcion in ["1","2","3","4","5"]:
            num1 = float(input("ingrese su valor del numero 1:"))
            num2 = float(input("ingrese su valor del numero 2:"))

            if opcion == "1":
                print("La suma es:",suma(num1,num2))
            elif opcion == "2":
                print("La resta es:",resta(num1,num2))
            elif opcion == "3":
                print("La multiplicacion es:",multiplicacion(num1,num2))
            elif opcion == "4":
                print("La divicion es:",divicion(num1,num2))
            elif opcion == "5":
                print("El modulo es:",modulo(num1,num2))
calculadora()
        
   
