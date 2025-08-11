from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self):
        self.tablero = Tablero()
        self.jugadores = [
            Jugador("Jugador 1", "X"),
            Jugador("Jugador 2", "O")
        ]
        self.turno_actual = 0

    def ocupar_una_de_las_casillas(self, fil, col):
        jugador = self.jugadores[self.turno_actual]

        # Validar rangos
        if not (0 <= fil <= 2 and 0 <= col <= 2):
            raise ValueError("Fila y columna deben estar entre 0 y 2")

        self.tablero.poner_la_ficha(fil, col, jugador.ficha)

        if self.hay_ganador():
            self.tablero.mostrar()
            print(f"¡Ganó {jugador.nombre}!")
            exit()

        if self.tablero.esta_lleno():
            self.tablero.mostrar()
            print("¡Empate!")
            exit()

        self.turno_actual = 1 - self.turno_actual

    def hay_ganador(self):
        c = self.tablero.contenedor

        # Filas
        for fila in c:
            if fila[0] != "" and fila[0] == fila[1] == fila[2]:
                return True

        # Columnas
        for col in range(3):
            if c[0][col] != "" and c[0][col] == c[1][col] == c[2][col]:
                return True

        # Diagonales
        if c[0][0] != "" and c[0][0] == c[1][1] == c[2][2]:
            return True
        if c[0][2] != "" and c[0][2] == c[1][1] == c[2][0]:
            return True

        return False
