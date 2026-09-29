from Contacto import Contacto


class Agenda:
    def __init__(self):


    def guardar_contacto(respuesta=None):

        nombre = input("Nombre de contacto: :")
        while nombre == "":
            nombre = input("Nombre de contacto: :")
        apellido = input("Apellido de contacto: ")
        while apellido == "":
            apellido = input("Apellido de contacto: ")
        telefono1 = input("Telefono de contacto: ")
        while telefono == "":
            telefono = input("Telefono de contacto: ")

        print("¿Tiene un segundo telefono?")
        if respuesta == input():
            telefono2 = input("Telefono de contacto: ")
        else:
            telefono2 = None

        telefono2 = str(input("Telefono de contacto: "))
        direccion = input("Direccion de contacto: ")
        while direccion == "":
            direccion = input("Direccion de contacto: ")

        c = Contacto(nombre, apellido, telefono1, telefono2, direccion)


if __name__ == '__main__':
    agenda = Agenda()