import unittest

def sumar(a, b):
    return a + b

class TestSumar(unittest.TestCase):
    def test_suma_positiva(self):
        resultado = sumar(3, 5)
        self.assertEqual(resultado, 8)

    def test_suma_negativa(self):
        resultado = sumar(-3, -5)
        self.assertEqual(resultado, -8)

    def test_suma_cero(self):
        resultado = sumar(0, 0)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()