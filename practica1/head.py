from pathlib import Path

def head():
    archivo = Path("fundacion.txt")
    num_lineas = int(input("Dime hasta que linea quieres imprimir: "))

    with open(archivo) as f:
        file_lines = f.readlines()
        for i, linea in enumerate(file_lines):
            if i < num_lineas + 1:
                # end="" evita que imprima un salto de línea doble
                # (ya que readlines() incluye el \n del archivo)
                print(f"{i}: {linea}", end="")