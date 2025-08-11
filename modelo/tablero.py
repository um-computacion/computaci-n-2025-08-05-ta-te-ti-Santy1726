from exceptions import PosOcupadaException

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("Posición ocupada!")

    def mostrar(self):
        print("\n  0   1   2")
        for i, fila in enumerate(self.contenedor):
            print(i, " | ".join(c if c != "" else " " for c in fila))
            if i < 2:
                print("  ---------")

    def esta_lleno(self):
        return all(c != "" for fila in self.contenedor for c in fila)

