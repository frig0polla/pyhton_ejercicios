from Contacto import Contacto
import csv

class Agenda:
    def __init__(self):
        self.ruta = 'guardado.csv'

    def guardar_contacto(self):

        nombre = input("Nombre de contacto:")
        while nombre == "":
            nombre = input("Nombre de contacto: :")
        apellidos = input("Apellidos del contacto: ")
        while apellidos == "":
            apellidos = input("Apellidos del contacto: ")
        telefono1 = input("Telefono de contacto: ")
        while telefono1 == "":
            telefono1 = input("Telefono de contacto: ")

        respuesta = input("Tiene segundo telefono?")
        if respuesta.lower() == 'si':
            telefono2 = input("Telefono de contacto: ")
        else:
            telefono2 = None

        direccion = input("Direccion de contacto: ")
        while direccion == "":
            direccion = input("Direccion de contacto: ")

        c = Contacto(nombre, apellidos, telefono1, telefono2, direccion)

        with open(self.ruta, 'a', newline='', encoding="utf-8") as csvf:
            escritor = csv.writer(csvf)
            escritor.writerow([c.nombre, c.apellidos, c.telefono1, c.telefono2, c.direccion])


    def modificar_contacto(self):
        contactos = []
        with open (self.ruta, 'r', encoding="utf-8") as csvf:
            lector = csv.reader(csvf)
            for fila in lector:
                contacto = Contacto(*fila)
                contactos.append(contacto)

            for i, contacto in enumerate(contactos, start=1):
                print(i, contacto.nombre, contacto.apellidos, contacto.telefono1, contacto.telefono2, contacto.direccion)

        try:
            numero = int(input("ID o numero de contacto: "))
        except ValueError:
            numero = input("Tienes que escribir un numero: ")
        else:
            if contacto_elegido = contactos[numero-1]
            else:
                print("El numero no existe")





if __name__ == '__main__':
    agenda = Agenda()
    agenda.modificar_contacto()