import Agenda

if __name__ == '__main__':
    agenda = Agenda.Agenda()


    print("1 - Guardar nuevo contacto")
    print("2 - Modificar datos de un contacto existente")
    print("3 - Eliminar contacto")
    print("4 - Buscar contacto existente")
    print("5 - Mostrar contactos")
    print("6 - Salir")

    option = int(input())
    agenda = Agenda.Agenda()

    match option:
        case 1:
            agenda.guardar_contacto()



