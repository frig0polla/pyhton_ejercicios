from head import head
from cp import cp
from cut import cut
from wc import wc

if __name__ == "__main__":
    print("Elije un programa")
    print("1. Head")
    print("2. CP")
    print("3. Cut")
    print("4. WC")

    try:
        opcion = int(input("> "))
        match opcion:
            case 1:
                head()
            case 2:
                cp()
            case 3:
                cut()
            case 4:
                wc()
            case _:
                print("Opción no válida. Elije un programa\n")
    except ValueError:
        print("Por favor, introduce un número.")

    # Mantenido de tu código original
    fichero = input("\nDame el nombre de fichero: ")