import unittest
from domeniu.student import Student

class testStudentUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = Student(0, "Stefania Beldean", 444)

    def test_getNume(self):
        self.assertEqual(self.s1.getIdEntitate(), 0)

    def test_setNume(self, nume = "Antonia"):
        self.assertEqual(self.s1.setNume(nume), None)
        self.assertEqual(self.s1.getNume(), "Antonia")

    def test_getGrup(self):
        self.assertEqual(self.s1.getGrup(), 444)

    def test_setGrup(self, grup = 311):
        self.assertEqual(self.s1.setGrup(grup), None)
        self.assertEqual(self.s1.getGrup(), 311)

    def tearDown(self) -> None:
        del self.s1

if __name__ == '__main__':
    unittest.main()
