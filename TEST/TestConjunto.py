import unittest
from SRC.LOGICA.Conjunto import Conjunto
class TestConjunto( unittest.TestCase ):
    def test_conjunto_vacio_retornarnone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_vacio_retornarnone(self):
        conjunto = Conjunto([])
        self.assertIsNone(elemento.promedio())
