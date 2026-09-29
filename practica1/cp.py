from pathlib import Path


def cp():
    archivo = Path("fundacion.txt")
    lines = []

    with open(archivo) as f:
        lines = f.readlines()

    with open("copia1", "w") as f:
        f.writelines(lines)

    print("Copia realizada!")