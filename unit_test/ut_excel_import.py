import unittest

from cmd_controller import CmdController
from cmd_view import CmdView
from db_pickle_view import DBPickleView
from db_view import DBView
from excel_import_view import ExcelView
from matplot_view import MatPlotView


class ExcelImportingTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.con = CmdController(CmdView(), ExcelView(), DBView(),
                                 MatPlotView(), DBPickleView())

    def tearDown(self):
        # be executed after each test case
        print('End of Test\n\n')

    def test_file_that_doesnt_exist(self):
        actual = self.con.import_from_excel(
            r"..\TestingDir\AnotherDir\TestFile.xls")
        self.assertEqual(['That file or directory does not exist'], actual)

    def test_ImportAFile_ThatDoesntExist(self):
        expected = ['Invalid use of the command']
        actual = self.con.import_from_excel("TestFile")
        self.assertEqual(expected, actual)

    def test_import_a_valid_file(self):
        actual = self.con.import_from_excel("TestFile.xls")
        self.assertEqual([['A123', 'M', 16.0, 123.0, 'Normal', 23.0,
                           '20-10-2000'],
                          ['A124', 'F', 16.0, 124.0, 'Normal', 24.0,
                           '21-11-2000'],
                          ['A125', 'M', 22.0, 129.0, 'Underweight', 29.0,
                           '10-9-1994'],
                          ['A126', 'M', 22.0, 129.0, 'Underweight', 29.0,
                           '10-9-1994'],
                          ['A127', 'M', 24.0, 127.0, 'Overweight', 27.0,
                           '8-7-1992'],
                          ['A128', 'F', 23.0, 128.0, 'Overweight', 28.0,
                           '9-8-1993'],
                          ['A129', 'M', 22.0, 129.0, 'Underweight', 29.0,
                           '10-9-1994'],
                          ['A130', 'F', 21.0, 130.0, 'Underweight', 30.0,
                           '11-10-1995'],
                          ['A131', 'M', 36.0, 131.0, 'Normal', 31.0,
                           '3-4-1980'],
                          ['A132', 'F', 31.0, 132.0, 'Overweight', 32.0,
                           '8-7-1985']], actual)

    def test_importAndValidate_aTestFile_withAllValidData(self):
        self.con.import_from_excel(r"..\TestingDir\FullRangeValidTestFile.xls")
        actual = self.con.validate_data()
        self.assertEqual(actual, "Data is valid you can now save")
