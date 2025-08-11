import unittest
from tablero import Tablero
from exceptions import PosOcupadaException

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_poner_ficha_valida(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")

    def test_poner_ficha_posicion_ocupada(self):
        self.tablero.poner_la_ficha(1, 1, "O")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(1, 1, "X")

    def test_esta_lleno(self):
        
        self.assertFalse(self.tablero.esta_lleno())
        for fila in range(3):
            for col in range(3):
                self.tablero.contenedor[fila][col] = "X"
        self.assertTrue(self.tablero.esta_lleno())

if __name__ == "__main__":
    unittest.main()
