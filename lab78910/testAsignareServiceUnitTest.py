import unittest

from domeniu.asignare import Asignare
from domeniu.problema import Problema
from domeniu.student import Student
from repository.repositoryJson import RepositoryJson
from service.asignareService import AsignareService


class testAsignareService(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = Student(0, "Stefania Beldean", 444)
        self.s2 = Student(1, "Alex Trifan", 444)
        self.s3 = Student(2, "Alin Aluas", 444)
        self.p1 = Problema(0, "descriere", "nush")
        self.asignare = Asignare(0, 0, 0, 10)
        self.studentRepository = RepositoryJson("testStudentiUnitTest.json")
        self.problemaLaboratorRepository = RepositoryJson("testProblemaUnitTest.json")
        self.asignareRepository = RepositoryJson("testAsignareUnitTest.json")
        self.asignareService = AsignareService(self.asignareRepository, self.studentRepository, self.problemaLaboratorRepository)
        with open("testStudentiUnitTest.json", 'w'):
            pass
        with open("testAsignareUnitTest.json", 'w'):
            pass

    def test_getAllAsignari(self):
        self.assertEqual(self.asignareService.getAllAsignari(), [])
        self.studentRepository.adauga(self.s1)
        self.problemaLaboratorRepository.adauga(self.p1)
        self.asignareService.adaugaAsignare(0, 0, 0, 10)
        self.assertEqual(len(self.asignareService.getAllAsignari()), 1)

    def test_adaugaAsignare(self, idAsignare = 0, idStudent = 0, idProblemaLaborator = 0, nota = 10):
        self.assertEqual(self.asignareService.getAllAsignari(), [])
        self.studentRepository.adauga(self.s1)
        self.problemaLaboratorRepository.adauga(self.p1)
        self.asignareService.adaugaAsignare(idAsignare, idStudent, idProblemaLaborator, nota)
        self.assertEqual(len(self.asignareService.getAllAsignari()), 1)

    def test_stergeAsignare(self, idAsignare = 0):
        self.assertEqual(self.asignareService.getAllAsignari(), [])
        self.studentRepository.adauga(self.s1)
        self.problemaLaboratorRepository.adauga(self.p1)
        self.asignareService.adaugaAsignare(0, 0, 0, 10)
        self.assertEqual(len(self.asignareService.getAllAsignari()), 1)
        self.asignareRepository.sterge(str(idAsignare))
        self.assertEqual(len(self.asignareService.getAllAsignari()), 0)

    def test_modificaAsignare(self, idAsignare = 0, idStudentNou = 1, idProblemaLaboratorNoua = 1, notaNoua = 7):
        self.assertEqual(self.asignareService.getAllAsignari(), [])
        self.studentRepository.adauga(self.s1)
        self.problemaLaboratorRepository.adauga(self.p1)
        self.asignareRepository.adauga(self.asignare)
        self.assertEqual(len(self.asignareService.getAllAsignari()), 1)
        self.asignare.setIdEntitate(idAsignare)
        self.asignare.setIdStudent(idStudentNou)
        self.asignare.setIdProblema(idProblemaLaboratorNoua)
        self.asignare.setNota(notaNoua)
        self.assertEqual(self.asignareService.getAllAsignari(), [self.asignare])

    def test_cautareAsignare(self, idAsignare = '0'):
        asignareService = AsignareService(self.asignareRepository, self.studentRepository, self.problemaLaboratorRepository)
        self.assertEqual(asignareService.getAllAsignari(), [])
        self.studentRepository.adauga(self.s1)
        self.problemaLaboratorRepository.adauga(self.p1)
        self.asignareRepository.adauga(self.asignare)
        self.assertEqual(asignareService.cautareAsignare(self.asignare.getIdEntitate()), self.asignare)

    def test_ordonare(self, idProblema = 0, param = "1"):
        self.assertEqual(self.asignareService.getAllAsignari(), [])
        self.studentRepository.adauga(self.s1)
        self.studentRepository.adauga(self.s2)
        self.studentRepository.adauga(self.s3)
        self.s1.setIdEntitate('0')
        self.s2.setIdEntitate('1')
        self.s3.setIdEntitate(2)
        self.problemaLaboratorRepository.adauga(self.p1)
        self.asignareService.adaugaAsignare(0, self.s1.getIdEntitate(), idProblema, 10)
        self.asignareService.adaugaAsignare(1, self.s2.getIdEntitate(), idProblema, 5)
        self.asignareService.adaugaAsignare(2, self.s3.getIdEntitate(), idProblema, 7)
        self.assertEqual(len(self.asignareService.getAllAsignari()), 3)
        lista = self.asignareService.ordonare(idProblema, param)
        self.assertEqual(len(lista), 1)
        lista2 = self.asignareService.ordonare(idProblema, "2")
        self.assertEqual(len(lista2), 1)

    def test_getStudentiCuMedieSubCinci(self):
        self.assertEqual(self.asignareService.getAllAsignari(), [])
        self.studentRepository.adauga(self.s1)
        self.studentRepository.adauga(self.s2)
        self.studentRepository.adauga(self.s3)
        self.s1.setIdEntitate('0')
        self.s2.setIdEntitate('1')
        # s3.setIdEntitate(2)
        self.problemaLaboratorRepository.adauga(self.p1)
        self.asignareService.adaugaAsignare(0, self.s1.getIdEntitate(), 0, 7)
        self.asignareService.adaugaAsignare(1, self.s2.getIdEntitate(), 0, 8)
        self.asignareService.adaugaAsignare(2, self.s3.getIdEntitate(), 0, 3)
        lista = self.asignareService.getStudentiCuMedieSubCinci()
        self.assertEqual(lista, [(self.s1.getNume(), 3)])

    def tearDown(self) -> None:
        '''del self.studentRepository
        del self.problemaLaboratorRepository
        del self.asignareRepository
        del self.asignareService
        del self.asignare
        del self.s1
        del self.s2
        del self.s3
        del self.p1'''
        pass


if __name__ == '__main__':
    unittest.main()