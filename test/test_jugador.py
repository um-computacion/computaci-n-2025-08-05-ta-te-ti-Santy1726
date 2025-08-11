import unittest
from jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_crear_jugador(self):
        j = Jugador("Ana", "X")
        self.assertEqual(j.nombre, "Ana")
        self.assertEqual(j.ficha, "X")

    def test_str(self):
        j = Jugador("Carlos", "O")
        self.assertEqual(str(j), "Carlos (O)")

if __name__ == "__main__":
    unittest.main()
