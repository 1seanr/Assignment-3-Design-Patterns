import unittest

from cmd_controller import CmdController
from cmd_view import CmdView
from db_pickle_view import DBPickleView
from db_view import DBView
from excel_import_view import ExcelView
from matplot_view import MatPlotView


class PickleSaveAndLoadTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.con = CmdController(CmdView(), ExcelView(), DBView(),
                                 MatPlotView(), DBPickleView())

    def tearDown(self):
        # be executed after each test case
        print('End of Test\n\n')

    def test_savingUsingPickle_invalidName(self):
        actual = self.con.db_pickle('s', '')
        self.assertEqual("Invalid use of the command", actual)

    def test_savingUsingPickle_shouldSaveAsTest(self):
        actual = self.con.db_pickle('s', 'test')
        self.assertEqual(["Saved Successfully as: test.pickle"], actual)

    def test_loadingWithPickle_withoutAFileName(self):
        actual = self.con.db_pickle('l', 'add')
        self.assertEqual("Invalid use of the command please enter "
                         "'replace'/'add' and a filename", actual)

    def test_loadingWithPickle_withoutValid_addOrReplaceParameter(self):
        actual = self.con.db_pickle('l', 'test')
        self.assertEqual("Invalid command please use either 'replace' or "
                         "'add'", actual)

    def test_loadingWithPickle_noParameters(self):
        actual = self.con.db_pickle('l', '')
        self.assertEqual("Invalid use of the command", actual)

    def test_loadingWithPickle_fileThatDoesntExist(self):
        actual = self.con.db_pickle('l', 'add TestFileThatDoesntExist')
        self.assertEqual(["File not found"], actual)

    def test_loadingWithPickle_importsAndReplaces(self):
        self.con.db_pickle('s', 'test')
        self.con.db_pickle('l', 'replace test')
        actual = self.con.load_from_db('')
        expected = [('T123', 'M', 20, 654, 'Normal', 56, '1996-10-18'),
                    ('G834', 'M', 54, 213, 'Overweight', 566, '1990-12-4'),
                    ('S931', 'F', 80, 986, 'Obesity', 852, '2001-5-1'),
                    ('P912', 'M', 34, 43, 'Underweight', 135, '1998-7-26'),
                    ('B720', 'F', 67, 867, 'Normal', 741, '1993-1-6')]
        self.assertEqual(expected, actual)

    def test_loadingWithPickle_importsAndAdds(self):
        self.con.db_pickle('s', 'test')
        self.con.db_pickle('l', 'add test')
        actual = self.con.load_from_db('')
        expected = [('T123', 'M', 20, 654, 'Normal', 56, '1996-10-18'),
                    ('G834', 'M', 54, 213, 'Overweight', 566, '1990-12-4'),
                    ('S931', 'F', 80, 986, 'Obesity', 852, '2001-5-1'),
                    ('P912', 'M', 34, 43, 'Underweight', 135, '1998-7-26'),
                    ('B720', 'F', 67, 867, 'Normal', 741, '1993-1-6')]
        self.assertEqual(expected, actual)
