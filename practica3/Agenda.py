import csv
from xml.etree.ElementTree import SubElement

from Contacto import Contacto
import xml.etree.ElementTree as et

class Agenda:
    def __init__(self):
        self.ruta = r'C:\Users\saerg\Documentos\DAM\pyhton_ejercicios\practica2\guardado.csv'



    def hacer_copia(self):
        contactos = []
        raiz = et.Element('Contactos')
        with open(self.ruta) as csvfile:
            lector = csv.reader(csvfile)
            for fila in lector:
                contacto = Contacto(*fila)
                contactos.append(contacto)

        for c in contactos:
            contacto = et.SubElement(raiz, 'contacto')
            et.SubElement(contacto, 'nombre').text = c.nombre
            et.SubElement(contacto, 'apellidos').text = c.apellidos
            et.SubElement(contacto, 'direccion').text = c.direccion
            et.SubElement(contacto, 'telefono1').text = c.telefono1
            et.SubElement(contacto, 'telefono2').text = c.telefono2

        arbol = et.ElementTree(raiz)
        et.indent(arbol)
        arbol.write("agenda.xml", encoding="utf-8", xml_declaration=True)

        print("El archivo se ha creado correctamente")

    def guardar_contacto(self):
        arbol = et.parse("agenda.xml")
        raiz = arbol.getroot()
        print("Añada los datos del contacto a guardar")
        contacto = et.SubElement(raiz, 'contacto')
        et.SubElement(contacto, 'nombre').text = input("Ingrese el nombre del contacto")
        et.SubElement(contacto, 'apellidos').text = input("Ingrese los apellidos del contacto")
        et.SubElement(contacto, "direccion").text = input("Ingrese el direccion del contacto")
        et.SubElement(contacto, 'telefono1').text = input("Ingrese el telefono del contacto")
        respuesta = input("¿El usuario tiene telefono secundario?")

        if respuesta.lower() == "si":
            et.SubElement(contacto, 'telefono2').text = input("Ingrese el telefono secundario del contacto")
        else :
            et.SubElement(contacto, 'telefono2').text = ""

        arbol = et.ElementTree(raiz)
        et.indent(arbol)
        arbol.write("agenda.xml", encoding="utf-8", xml_declaration=True)

    def mostrar_contacto(self):
        arbol = et.parse("agenda.xml")
        raiz = arbol.getroot()
        lista_contactos = raiz.findall('contacto')
        lista_ordeanada = sorted(lista_contactos, key=lambda c: c.find('nombre').text.lower())
        for contacto in lista_ordeanada:
            print("Nombre: ", contacto.find('nombre').text)
            print("Apellidos: ", contacto.find('apellidos').text)
            print("Dirección: ",contacto.find('direccion').text)
            print("Telefono: ", contacto.find('telefono1').text)
            print("Telefono Secundario: ", contacto.find('telefono2').text)
            print("======================================================")

    def modificar_contacto(selfself):
        arbol = et.parse("agenda.xml")
        raiz = arbol.getroot()
        lista = raiz.findall('contacto')
        lista_ordeanada = sorted(lista, key=lambda c: c.find('nombre').text.lower())
        for indice, i in enumerate(lista_ordeanada):
            print(indice, i.find('nombre').text, i.find('apellidos').text,
                  i.find('direccion').text,i.find('telefono1').text,i.find('telefono2').text)

        eleccion = int(input("[!] - Selecciona un contacto a modificar"))
        contacto_elegido = lista_ordeanada[eleccion]
        print(f"""
                    [1] - Nombre del contacto
                                Nombre actual: {contacto_elegido.find('nombre').text}
                    [2] - Apellidos del contacto
                                Apellidos actuales: {contacto_elegido.find('apellidos').text}
                    [3] - Direccion del contacto
                                D
                    [4] - Telefono del contacto

                    [5] - Telefono Secundario

                """)
        option = int(input(" sysadmin@agenda:~$ 'Elige que quieres cambiar':"))
        match option:
            case 1:
                contacto_elegido.find('nombre').text = input("Ingrese el nombre del contacto")
            case 2:
                contacto_elegido.find('apellidos').text = input("Ingrese los nuevos apellidos del contacto")
            case 3:
                contacto_elegido.find('telefono1').text = input("Ingrese el nuevo telefono del contacto")
            case 4:
                contacto_elegido.find('telefono2').text = input("Ingrese el nuevo telefono secundario del contacto")
            case 0:
                print("[!] - Elección no válida")


