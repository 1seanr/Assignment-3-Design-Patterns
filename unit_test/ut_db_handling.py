import unittest

from cmd_controller import CmdController
from cmd_view import CmdView
from db_pickle_view import DBPickleView
from db_view import DBView
from excel_import_view import ExcelView
from matplot_view import MatPlotView


class DBSavingAndLoadingTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.con = CmdController(CmdView(), ExcelView(), DBView(),
                                 MatPlotView(), DBPickleView())

    def tearDown(self):
        # be executed after each test case
        print('End of Test\n\n')

    def test_loadFromDb_WithNoParameters(self):
        expected = [('T123', 'M', 20, 654, 'Normal', 56, '1996-10-18'),
                    ('G834', 'M', 54, 213, 'Overweight', 566, '1990-12-4'),
                    ('S931', 'F', 80, 986, 'Obesity', 852, '2001-5-1'),
                    ('P912', 'M', 34, 43, 'Underweight', 135, '1998-7-26'),
                    ('B720', 'F', 67, 867, 'Normal', 741, '1993-1-6')]
        actual = self.con.load_from_db('')
        self.assertEqual(expected, actual)

    def test_loadFromDb_WithAValidCondition(self):
        expected = [('G834',), ('S931',), ('P912',), ('B720',)]
        actual = self.con.load_from_db('EMPID Age>20')
        self.assertEqual(expected, actual)

    def test_loadFromDb_withInvalidCommands(self):
        expected = 'Invalid use of the command'
        actual = self.con.load_from_db("This is broken")
        self.assertEqual(expected, actual)

    def test_SaveToDb_WithValidCommands(self):
        expected = 'Saved successfully'
        self.con.import_from_excel("TestingDir\FullRangeValidTestFile.xls")
        self.con.validate_data()
        actual = self.con.save_to_db()
        self.assertEqual(expected, actual)

    def test_SaveToDb_WithoutValidating(self):
        expected = "Please validate the data using the 'validate' command"
        self.con.import_from_excel("TestingDir\FullRangeValidTestFile.xls")
        actual = self.con.save_to_db()
        self.assertEqual(expected, actual)
