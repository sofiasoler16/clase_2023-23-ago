import unittest

from app.multi import multiplicacion

class TestMulti(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multiplicacion(2,5),10)

if __name__ == "__main__":
    unittest.main()