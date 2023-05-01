from tests.TestStudent import testStudent,testStudentSetteri
from tests.TestStudentRepository import testAdaugaStudentRepository,testModificaStudentRepository, testStergeStudentRepository
from tests.TestStudentService import testAdaugaStudentService, testModificaStudentService, testStergeStudentService


def testAll():
    testStudent()
    testStudentSetteri()

    testAdaugaStudentRepository()
    testModificaStudentRepository()
    testStergeStudentRepository()

    testAdaugaStudentService()
    testModificaStudentService()
    testStergeStudentService()
