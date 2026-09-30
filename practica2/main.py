import Agenda

if __name__ == '__main__':
    agenda = Agenda.Agenda()




    while(True):
        print("╔══════════════════════════════════════════════════════╗")
        print("║                 AGENDA DE CONTACTOS                  ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║  1 │ Guardar nuevo contacto                          ║")
        print("║  2 │ Modificar datos de un contacto existente        ║")
        print("║  3 │ Eliminar contacto                               ║")
        print("║  4 │ Buscar contacto existente por nombre            ║")
        print("║  5 │ Mostrar contactos ordenados alfabéticamente     ║")
        print("║  6 │ Salir                                           ║")
        print("╚══════════════════════════════════════════════════════╝")
        option = int(input("  Elige una opción ➜ "))
        agenda = Agenda.Agenda()


        match option:
            case 1:
                agenda.guardar_contacto()
            case 2:
                agenda.modificar_contacto()
            case 3:
                agenda.eliminar_contacto()
            case 4:
                agenda.buscar_contacto()
            case 5:
                agenda.contactos_ordenados()
            case 6:
                print("Hasta la próxima crack")
                break




