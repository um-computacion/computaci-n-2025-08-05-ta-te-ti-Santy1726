from tateti import Tateti
from exceptions import PosOcupadaException

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()

    while True:
        juego.tablero.mostrar()
        jugador = juego.jugadores[juego.turno_actual]
        print(f"Turno de {jugador.nombre} ({jugador.ficha})")

        try:
            fil = int(input("Ingrese fila: "))
            col = int(input("Ingrese columna: "))
            juego.ocupar_una_de_las_casillas(fil, col)
        except PosOcupadaException as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()






