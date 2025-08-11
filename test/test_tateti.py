import unittest
from tateti import Tateti
from exceptions import PosOcupadaException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.juego = Tateti()

    def test_turno_cambio(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno_actual, 1)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.assertEqual(self.juego.turno_actual, 0)

    def test_posicion_ocupada(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(0, 0)

    def test_ganador_fila(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(1, 0)  # O
        self.juego.ocupar_una_de_las_casillas(0, 1)  # X
        self.juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.juego.ocupar_una_de_las_casillas(0, 2)  # X gana

        self.assertTrue(self.juego.hay_ganador())

    def test_ganador_diagonal(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(0, 1)  # O
        self.juego.ocupar_una_de_las_casillas(1, 1)  # X
        self.juego.ocupar_una_de_las_casillas(0, 2)  # O
        self.juego.ocupar_una_de_las_casillas(2, 2)  # X gana

        self.assertTrue(self.juego.hay_ganador())

if __name__ == "__main__":
    unittest.main()
