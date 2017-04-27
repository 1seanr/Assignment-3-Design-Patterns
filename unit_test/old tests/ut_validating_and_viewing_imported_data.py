import unittest

from cmd_controller import CmdController
from cmd_view import CmdView
from db_pickle_view import DBPickleView
from db_view import DBView
from excel_import_view import ExcelView
from matplot_view import MatPlotView


class ValidatingAndViewingTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.con = CmdController(CmdView(), ExcelView(), DBView(),
                                 MatPlotView(), DBPickleView())

    def tearDown(self):
        # be executed after each test case
        self.con.close_db()
        print('End of Test\n\n')

    def test_importAndValidate_aTestFile_withAllBadData(self):
        print("c2")
        self.con.import_from_excel("..\TestingDir\FullRangeInValidTestFile.xls")
        actual = self.con.validate_data()
        self.assertEqual("Data not valid please correct it\n Invalid data on "
                         "rows: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 "
                         "18 19 20 21 22 23 24 25 26 27 28 29 30 ", actual)

    def test_importAFile_thatIsInADirectory_and_viewTheData(self):
        self.con.import_from_excel("..\TestingDir\TestFile.xls")
        actual = self.con.view()
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

    def test_importAFile_and_viewTheData(self):
        self.con.import_from_excel("..\TestFile.xls")
        actual = self.con.view()
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