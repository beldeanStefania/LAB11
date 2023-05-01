import unittest

from domeniu.student import Student
from repository.repositoryInMemory import RepositoryInMemory


class testRepositoryinMemoryUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = Student(0, "Stefania Beldean", 444)
        self.s2 = Student(1, "Alex Trifan", 555)
        self.s3 = Student(2, "Alin Aluas", 666)
        self.repo = RepositoryInMemory()

    def test_getAll(self):
        self.repo.adauga(self.s1)
        self.repo.adauga(self.s2)
        self.repo.adauga(self.s3)
        list = [self.s1, self.s2, self.s3]
        self.assertEqual(len(self.repo.getAll()), 3)
        self.assertEqual(self.repo.getAll(), list)

    def test_getById(self, idEntitate = 1):

        self.repo.adauga(self.s1)
        self.repo.adauga(self.s2)
        self.repo.adauga(self.s3)
        self.assertEqual(self.repo.getById(idEntitate), self.s2)
        self.assertNotEqual(self.repo.getById(idEntitate), self.s1)

    def test_adauga(self, s1 = Student(0, "Stefania Beldean", 444)):
        self.repo = RepositoryInMemory()
        self.repo.adauga(s1)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.assertEqual(self.repo.getById(0), s1)

    def test_sterge(self, idEntitate = '0'):
        self.repo.adauga(self.s1)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.assertEqual(self.repo.getById(0), self.s1)
        self.repo.sterge(self.s1.getIdEntitate())
        self.assertEqual(len(self.repo.getAll()), 0)
        self.assertRaises(TypeError, self.repo.getById(idEntitate))

    def test_modifica(self, idEntitate = 0, s1 = Student(0, "Stefania Beldean", 444)):
        self.repo.adauga(s1)
        self.assertEqual(self.repo.modifica(0, self.s2), None)
        self.assertEqual(self.repo.getById(idEntitate), self.s2)
        self.assertRaises(TypeError, self.repo.getById(1))
        self.assertNotEqual(self.repo.getById(idEntitate), self.s1)

    def test_cauta(self, idEntitate = 0):
        self.repo.adauga(self.s1)
        self.assertEqual(self.repo.cauta(idEntitate), self.s1)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()