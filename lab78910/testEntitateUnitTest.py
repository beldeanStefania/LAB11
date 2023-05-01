import unittest
from domeniu.entitate import Entitate

class testEntitateUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.e = Entitate(5)

    def test_getIdEntitate(self):
        self.assertEqual(self.e.getIdEntitate(), 5)

    def test_setIdEntitate(self, id_nou = 10):
        self.assertEqual(self.e.setIdEntitate(id_nou), None)
        self.assertEqual(self.e.getIdEntitate(), 10)

if __name__ == '__main__':
    unittest.main()