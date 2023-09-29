class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

persona = Persona("Juan")
print(persona.nombre)

class Lista:
    def __init__(self):
        self.lista = []

    def agregar(self, elemento):
        self.lista.append(elemento)

lista = Lista()
lista.agregar(1)
lista.agregar(2)
print(lista.lista)


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

producto = Producto("Televisor", 1000, 10)
print(producto.nombre)
print(producto.precio)
print(producto.stock)
