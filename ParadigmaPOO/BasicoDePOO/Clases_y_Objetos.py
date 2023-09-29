class Celular ():
    marca = "Motorola"
    modelo = "G32"
    camara = "48MP"



Celular = Celular()
Celular2  = Celular()
Celular3  = Celular()
Celular4  = Celular()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

    def es_mayor_de_edad(self):
        return self.edad >= 18

persona = Persona("Juan", 25)
persona.saludar()

print(persona.es_mayor_de_edad())

##Practico
class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad

    def get_saldo(self):
        return self.saldo

cuenta = CuentaBancaria("123456789", 1000)
cuenta.depositar(500)
print(cuenta.get_saldo())
