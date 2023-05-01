import unittest

from domeniu.student import Student
from repository.repositoryJson import RepositoryJson


class testRepositortJson(unittest.TestCase):
    def setUp(self) -> None:

        self.s1 = Student(0, "Stefania Beldean", 444)
        self.s2 = Student(1, "Alex Trifan", 555)
        self.studentRepositoryTest = RepositoryJson("testStudentiUnitTest.json")
        with open("testStudentiUnitTest.json", 'w'):
            pass

    def test___readFile(self):
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 0)

    def test___writeFile(self):
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 0)
        self.studentRepositoryTest.adauga(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 1)

    def test_loadFromFile(self):
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 0)
        self.s1 = Student(0, "Stefania Beldean", 444)
        self.studentRepositoryTest.adauga(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 1)
        self.studentRepositoryTest.loadFromFile()
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 1)

    def test_read(self):
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 0)
        self.studentRepositoryTest.adauga(self.s1)
        self.assertEqual(self.studentRepositoryTest.getById(0), self.s1)

    def test_adauga(self):
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 0)
        self.studentRepositoryTest.adauga(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 1)

        self.studentRepositoryTest.adauga(self.s2)
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 2)

    def test_sterge(self):
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 0)
        self.studentRepositoryTest.adauga(self.s1)
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 1)
        self.studentRepositoryTest.adauga(self.s2)
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 2)
        self.studentRepositoryTest.sterge('1')
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 1)
        self.studentRepositoryTest.sterge('0')
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 0)
        #self.assertEqual(len(self.studentRepositoryTest.getAll()), 2)


    def test_modifica(self):
        self.assertEqual(len(self.studentRepositoryTest.getAll()), 0)
        s1 = Student(0, "Stefania Beldean", 444)
        self.studentRepositoryTest.adauga(s1)
        s1.setNume("test")
        self.assertEqual(self.studentRepositoryTest.getById(s1.getIdEntitate()), s1)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()