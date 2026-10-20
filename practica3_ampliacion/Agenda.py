import csv
import xml
from xml.etree.ElementTree import Element

from Contacto import Contacto
import xml.etree.ElementTree as et

class Agenda:
    def __init__(self):
        self.ruta = './guardado.csv'

    def csv_to_xml(self):
        contactos = []
        raiz =  et.Element('Contactos')
        with open(self.ruta) as csvfile:
            lect = csv.reader(csvfile)
            for fila in lect:
                contacto = Contacto(*fila)
                contactos.append(contacto)

        for c in contactos:
            '''contacto.set('atributo',2 )'''
            contacto = et.SubElement(raiz, 'contacto')
            contacto.set('nombre', c.nombre)
            contacto.set('apellidos', c.apellidos)
            contacto.set('direccion', c.direccion)
            contacto.set('telefono1', c.telefono1)
            contacto.set('telefono2', c.telefono2)
        arbol = et.ElementTree(raiz)
        et.indent(arbol)
        arbol.write("agenda.xml", encoding="utf-8", xml_declaration=True)

    def guardar_contacto(self):
        arbol = et.parse("agenda.xml")
        raiz = arbol.getroot()
        print("Añada los datos del usuario al que desea agregar")
        contacto = et.SubElement(raiz, 'contacto')
        contacto.set('nombre', input("Escriba el nombre de usuario"))
        contacto.set('apellidos', input("Escriba los apellidos del usuario"))
        contacto.set("direccion", input("Escriba la dirección del usuario"))
        contacto.set('telefono1', input("Escriba el número de telefono del usuario"))
        respuesta = input("¿Tiene telefono secundario?")
        if respuesta.lower() == 'si':
            contacto.set('telefono2', input("Escriba el telefono secundario del usuario"))
        else :
            contacto.set('telefono2', ' ')
        arbol = et.ElementTree(raiz)
        et.indent(arbol)
        arbol.write("agenda.xml", encoding='utf-8', xml_declaration=True)

    def mostrar_contacto(self):
        arbol = et.parse("agenda.xml")
        raiz = arbol.getroot()
        lista = raiz.findall('contacto')
        for c in lista:
            nombre = c.attrib.get('nombre')
        lista_ordenada = sorted(lista, key=lambda p:p.get("nombre").lower())
        for c in lista_ordenada:
            print(c.attrib)

    def modificar_contacto(self):
        arbol = et.parse("agenda.xml")
        raiz = arbol.getroot()
        lista = raiz.findall('contacto')
        for c in lista:
            nombre = c.attrib.get('nombre')
        lista_ordenada = sorted(lista, key=lambda p: p.get("nombre").lower())
        for indice, i in enumerate(lista_ordenada):
            print(indice, i.attrib)
        eleccion = int(input("Selecciona el nombre del contacto: "))
        contacto_elegido = lista_ordenada[eleccion]
        print(f"""
                    [1] - Nombre del contacto
                                Nombre actual: {contacto_elegido.attrib.get('nombre')} 
                    [2] - Apellidos del contacto
                                Apellidos actuales: {contacto_elegido.attrib.get('apellidos')} 
                    [3] - Direccion del contacto
                                Dirección actual: {contacto_elegido.attrib.get('direccion')} 
                    [4] - Telefono del contacto
                                Telefono actual: {contacto_elegido.attrib.get('telefono1')} 
                    [5] - Telefono Secundario 
                                Telefono secundario actual: {contacto_elegido.attrib.get('telefono2')} 
                    """)
        opcion = int(input("Elige que quieres modificar: "))
        match opcion:
            case 1:
                contacto_elegido.set('nombre', input("Escriba el nuevo nombre: "))
            case 2:
                contacto_elegido.set('apellidos', input("Escriba el apellidos: "))
            case 3:
                contacto_elegido.set('direccion', input("Seleccione la nueva direccion:"))
            case 4:
                contacto_elegido.set('telefono1', input("Escriba el nuevo telefono1: "))
            case 5:
                contacto_elegido.set('telefono2', input("Escriba el nuevo telefono2: "))
            case 0:
                print("[!] - Elección no válida")
        arbol = et.ElementTree(raiz)
        et.indent(arbol)
        arbol.write("agenda.xml", encoding='utf-8', xml_declaration=True)

    def eliminar_contacto(self):
        arbol = et.parse("agenda.xml")
        raiz = arbol.getroot()
        lista = raiz.findall('contacto')
        lista_ordenada = sorted(lista, key=lambda c:
        c.find('nombre').text.lower())
        for c in lista_ordenada:
            print(c.attrib)
        contacto_elegido = int(input("Elija el contacto a eliminar"))
        raiz.remove(lista_ordenada[contacto_elegido])
        arbol = et.ElementTree(raiz)
        et.indent(arbol)
        arbol.write("agenda.xml", encoding='utf-8', xml_declaration=True)


