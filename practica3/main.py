import Agenda


def main():
    print("Iniciando el programa...")


if __name__ == "__main__":
    main()
    agenda = Agenda.Agenda()

    while True:
        print(r"""
    .-----------------------------------------.
    |      _   ___ ___ _  _ ___   _           |
    |     /_\ / __| __| \| |   \ /_\          |
    |    / _ \ (_ | _|| .` | |) / _ \         |
    |   /_/ \_\___|___|_|\_|___/_/ \_\        |
    |                                         |
    +-----------------------------------------+
    |                                         |
    |  [1] Crear agenda (SÓLO SI NO ESTÁ      |
    |      CREADO EL XML)                     |
    |  [2] Crear nuevo contacto               |
    |  [3] Mostrar contactos ordenados        |
    |  [4] Modificar contacto                 |
    |  [5] Eliminar contacto de la agenda     |
    |  [0] Salir de agenda                    |  
    |                                         |                                     
    '-----------------------------------------'
    """)

        opcion = input(" sysadmin@agenda:~$ 'Elige una opción':")

        match opcion:
            case "1":
                print("\n[+] Creando agenda...")
                agenda.hacer_copia()
            case "2":
                print("\n[+] Añadiendo nuevo contacto...")
                agenda.guardar_contacto()

            case "3":
                print("\n[+] Consultando datos...")
                agenda.mostrar_contacto()
            case "4":
                print("\n[!] Abriendo modo edición...")
                agenda.modificar_contacto()
            case "5":
                print("\nAbriendo modo eliminación...")
                agenda.eliminar_contacto()
            case "6":
                print("[!] - Saliendo...")
                break
            case _:
                print("\n[-] Error: Opción no válida.")

        input("\nPresiona ENTER para continuar...")