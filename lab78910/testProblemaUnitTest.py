import unittest
from domeniu.problema import Problema
from lab78910.domeniu import problema


class testProblemaUnitTest(unittest.TestCase):
  def setUp(self):
    self.problema = Problema(0, "suma a doua numere", "10.01.2023")

  def test_getDescriere(self):
    self.assertEqual(self.problema.getDescriere().split(), ['suma', 'a', 'doua', 'numere'])
    with self.assertRaises(TypeError):
      self.problema.getDescriere().split(4)

  def test_getDeadline(self):
    self.assertTrue(self.problema.getDeadline(), "10.01.2023")

  def test_setDescriere(self, descriere = "descriere"):
    self.assertEqual(self.problema.setDescriere(descriere), None)
    self.assertEqual(self.problema.getDescriere(), "descriere")

  def test_setDeadline(self, deadline = "24.08.2003"):
    p1 = Problema(0, "suma a doua numere", "10.01.2023")
    self.assertEqual(self.problema.setDeadline(deadline), None)
    self.assertEqual(self.problema.getDeadline(), "24.08.2003")

  def tearDown(self) -> None:
    pass

if __name__ == '__main__':
    unittest.main()