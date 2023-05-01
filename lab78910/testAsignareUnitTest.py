import unittest

from domeniu.asignare import Asignare
from domeniu.problema import Problema
from domeniu.student import Student


class testAsignareUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.problema = Problema(0, "suma a doua numere", "10.01.2023")
        self.student = Student(0, "Stefania Beldean", 444)
        self.asignare = Asignare(0, 0, 0, 10)

    def test_getIdStudent(self):
        self.assertEqual(self.student.getIdEntitate(), 0)

    def test_getIdProblema(self):
        self.assertEqual(self.asignare.getIdProblema(), 0)

    def test_getNota(self):
        self.assertEqual(self.asignare.getNota(), 10)

    def test_setIdStudent(self, idStudent = 2):
        self.assertEqual(self.asignare.setIdStudent(idStudent), None)
        self.assertEqual(self.student.setIdEntitate(idStudent), None)
        self.assertEqual(self.asignare.getIdStudent(), 2)
        self.assertTrue(self.student.getIdEntitate(), 2)

    def test_setIdProblema(self, nrLab_nrProblema = 2):
        self.assertEqual(self.asignare.setIdProblema(nrLab_nrProblema), None)
        self.assertEqual(self.asignare.getIdProblema(), 2)

    def test_setNota(self, nota = 7):
        self.assertEqual(self.asignare.setNota(nota), None)
        self.assertEqual(self.asignare.getNota(), 7)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
