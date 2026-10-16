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
        lista_ordenada = sorted(lista, key=lambda p:p.get("nombre").lower)
        print(lista_ordenada)

    '''/home/serlunrui/Documentos/react_native/pyhton_ejercicios/practica3_ampliacion/.venv/bin/python /home/serlunrui/Documentos/react_native/pyhton_ejercicios/practica3_ampliacion/main.py 
Traceback (most recent call last):
  File "/home/serlunrui/Documentos/react_native/pyhton_ejercicios/practica3_ampliacion/main.py", line 8, in <module>
    agenda.mostrar_contacto()
  File "/home/serlunrui/Documentos/react_native/pyhton_ejercicios/practica3_ampliacion/Agenda.py", line 57, in mostrar_contacto
    lista_ordenada = sorted(lista, key=lambda p:p.get("nombre").lower)
TypeError: '<' not supported between instances of 'builtin_function_or_method' and 'builtin_function_or_method''''