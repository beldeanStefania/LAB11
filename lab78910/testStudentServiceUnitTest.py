import unittest

from domeniu.student import Student
from repository.repositoryJson import RepositoryJson
from service.studentService import StudentService


class testStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.studentRepository = RepositoryJson("testStudentiUnitTest.json")
        self.asignareRepository = RepositoryJson("testAsignareUnitTest.json")
        self.studentService = StudentService(self.studentRepository, self.asignareRepository)
        self.s1 = Student(0, "Stefania Beldean", 444)
        with open("testStudentiUnitTest.json", 'w'):
            pass
        with open("testAsignareUnitTest.json", 'w'):
            pass

    def test_getAllStudenti(self):
        self.assertEqual(self.studentService.getAllStudenti(), [])
        self.studentService.adaugaStudent(0, "Stefania Beldean", 444)
        self.assertEqual(len(self.studentService.getAllStudenti()), 1)

    def test_adaugaStudent(self):
        self.assertEqual(self.studentService.getAllStudenti(), [])
        self.studentService.adaugaStudent(0, "Stefania Beldean", 444)
        self.assertEqual(len(self.studentService.getAllStudenti()), 1)
        self.studentService.adaugaStudent(1, "Alin Aluas", 444)
        self.assertEqual(len(self.studentService.getAllStudenti()), 2)

    def test_stergeStudent(self, idStudent = 1):
        self.assertEqual(self.studentService.getAllStudenti(), [])
        self.studentService.adaugaStudent(0, "Stefania Beldean", 444)
        self.assertEqual(len(self.studentService.getAllStudenti()), 1)
        self.studentService.adaugaStudent(1, "Alin Aluas", 444)
        self.assertEqual(len(self.studentService.getAllStudenti()), 2)
        self.studentRepository.sterge(str(idStudent))
        self.assertEqual(len(self.studentService.getAllStudenti()), 1)

    def test_modificaStudent(self, idStudent = 0, numeNou = "Alex Trifan", grupNou = 555):
        self.assertEqual(self.studentService.getAllStudenti(), [])
        self.studentRepository.adauga(self.s1)
        self.s1.setIdEntitate(idStudent)
        self.s1.setNume(numeNou)
        self.s1.setGrup(grupNou)
        self.assertEqual(self.studentService.getAllStudenti(), [self.s1])

    def test_cautaStudent(self):
        self.assertEqual(self.studentService.getAllStudenti(), [])
        self.studentRepository.adauga(self.s1)
        self.assertEqual(self.studentService.cautaStudent(self.s1.getIdEntitate()), self.s1)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()