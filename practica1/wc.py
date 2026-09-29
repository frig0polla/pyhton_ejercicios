from pathlib import Path


def wc():
    archivo = Path("listado-codigos-postales.csv")

    with open(archivo, newline='') as f:
        lines = f.readlines()
        caract_cont = 0
        word_cont = 0

        for line in lines:
            caract_cont += len(line)
            word_cont += len(line.split(" "))

    print(f"Total de caracteres: {caract_cont}")
    print(f"Total de palabras: {word_cont}")