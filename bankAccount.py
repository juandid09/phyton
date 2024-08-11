class cuenta_banco:
    def __init__(self, titular , balance):
        self.titular = titular
        self.balance = balance
        self.is_activo = True
    
    def deposito(self, monto):
        if self.is_activo:
           self.balance += monto
           print(f"se ha depositado {monto} y tu total es de: {self.balance}")

        else: 
           print("su cuenta esta inactiva")

    def retirar(self, monto):
        if self.is_activo:
           if monto <= self.balance:
              self.balance -= monto
              print(f"se ha retirado {monto} y tu total es de: {self.balance}")
           else:
            print("No tiene saldo su saldo es de:",self.balance )  

        else: 
           print("su cuenta esta inactiva")

    def desactivar_cuenta(self):
       self.is_activo = False
       print("su cuenta se desaptivo", self.is_activo)

    def activar_cuenta(self):
       if self.is_activo == True:
          print("su cuenta ya estaba activa")
       else:
        self.is_activo = True
        print("su cuenta se activo", self.is_activo)

cuenta1 = cuenta_banco("wilson",1000)
cuenta2 = cuenta_banco("kiara",5000)


#llamada a los metodos
cuenta1.deposito(200)
cuenta2.deposito(100)

cuenta1.desactivar_cuenta()
cuenta1.deposito(50)
cuenta1.activar_cuenta()
cuenta1.deposito(100)

cuenta1.retirar(50)

