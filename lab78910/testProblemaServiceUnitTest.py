import unittest

from domeniu.problema import Problema
from repository.repositoryJson import RepositoryJson
from service.problemaService import ProblemaLaboratorService


class testProblemaService(unittest.TestCase):
    def setUp(self) -> None:
        self.problemaLaboratorRepository = RepositoryJson("testProblemaUnitTest.json")
        self.asignareRepository = RepositoryJson("testAsignareUnitTest.json")
        self.problemaLaboratorService = ProblemaLaboratorService(self.problemaLaboratorRepository, self.asignareRepository)
        self.p1 = Problema(0, "descriere", "nush")
        with open("testProblemaUnitTest.json", 'w'):
            pass
        with open("testAsignareUnitTest.json", 'w'):
            pass

    def test_getAllProblemeLaborator(self):
        self.assertEqual(self.problemaLaboratorService.getAllProblemeLaborator(), [])
        self.problemaLaboratorService.adaugaProblemaLaborator(0, "descriere", "nush")
        self.assertEqual(len(self.problemaLaboratorService.getAllProblemeLaborator()), 1)

    def test_adaugaProblemaLaborator(self, idProblemaLaborator = 0, descriere = "descriere", deadline = "nush"):
        self.assertEqual(self.problemaLaboratorService.getAllProblemeLaborator(), [])
        self.problemaLaboratorService.adaugaProblemaLaborator(idProblemaLaborator, descriere, deadline)
        self.assertEqual(len(self.problemaLaboratorService.getAllProblemeLaborator()), 1)

    def test_stergeProblemaLaborator(self, idProblemaLaborator = 0):
        self.assertEqual(self.problemaLaboratorService.getAllProblemeLaborator(), [])
        self.problemaLaboratorService.adaugaProblemaLaborator(0, "descriere", "nush")
        self.assertEqual(len(self.problemaLaboratorService.getAllProblemeLaborator()), 1)
        self.problemaLaboratorRepository.sterge(str(idProblemaLaborator))
        self.assertEqual(len(self.problemaLaboratorService.getAllProblemeLaborator()), 0)

    def test_modificaProblemaLaborator(self, idProblemaLaborator = 0, descriereNoua = "descriere2", deadlineNou = "chiarNush"):
        self.assertEqual(self.problemaLaboratorService.getAllProblemeLaborator(), [])
        self.p1 = Problema(0, "descriere", "nush")
        self.problemaLaboratorRepository.adauga(self.p1)
        self.p1.setIdEntitate(idProblemaLaborator)
        self.p1.setDescriere(descriereNoua)
        self.p1.setDeadline(deadlineNou)
        self.assertEqual(self.problemaLaboratorService.getAllProblemeLaborator(), [self.p1])

    def test_cautareProblemaLaborator(self, idProblemaLaborator = 0):
        self.assertEqual(self.problemaLaboratorService.getAllProblemeLaborator(), [])
        self.problemaLaboratorRepository.adauga(self.p1)
        self.assertEqual(self.problemaLaboratorService.cautareProblemaLaborator(self.p1.getIdEntitate()), self.p1)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
