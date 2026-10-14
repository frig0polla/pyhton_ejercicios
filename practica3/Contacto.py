import Agenda
class Contacto:
    def __init__(self, nombre: str, apellidos: str, telefono1: str, telefono2: str|None, direccion: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.direccion = direccion

