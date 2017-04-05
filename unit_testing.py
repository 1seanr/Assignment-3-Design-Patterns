import unittest

from cmd_controller import CmdController
from cmd_view import CmdView
from db_pickle_view import DBPickleView
from db_view import DBView
from excel_import_view import ExcelView
from matplot_view import MatPlotView


class MainTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.con = CmdController(CmdView(), ExcelView(), DBView(),
                                 MatPlotView(), DBPickleView())
        print('')

    def tearDown(self):
        # be executed after each test case
        print('End of Test\n\n')

    def test_a3(self):
        print("a3")
        output = self.con.import_from_excel(
            "TestingDir\AnotherDir\TestFile.xls")
        self.assertEqual(['That file or directory does not exist'], output)

    def test_a5(self):
        print("a5")
        output = self.con.import_from_excel("TestingDir\\\TestFile.xls")
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
                           '8-7-1985']], output)

    def test_c1(self):
        print("c1")
        self.con.import_from_excel("TestingDir\FullRangeValidTestFile.xls")
        output = self.con.validate_data()
        self.assertEqual(output, "Data is valid you can now save")

    def test_c2(self):
        print("c2")
        self.con.import_from_excel("TestingDir\FullRangeInValidTestFile.xls")
        output = self.con.validate_data()
        self.assertEqual("Data not valid please correct it\n Invalid data on "
                         "rows: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 "
                         "18 19 20 21 22 23 24 25 26 27 28 29 30 ", output)

    def test_e1(self):
        print("e1")
        self.con.import_from_excel("TestingDir\TestFile.xls")
        output = self.con.view()
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
                           '8-7-1985']], output)

    def test_x1(self):
        print("x1")
        self.con.import_from_excel("TestingDir\TestFile.xls")
        self.con.validate_data()
        self.con.matplot_data()
        self.con.save_to_db()
        self.con.matplot_data()

    def test_f1(self):
        print("f1")
        output = self.con.db_pickle('s', '')
        self.assertEqual("Invalid use of the command", output)

    def test_f2(self):
        print("f2")
        output = self.con.db_pickle('s', 'test')
        self.assertEqual("Saved Successfully as: test.pickle", output)

    def test_f3(self):
        print("f3")
        output = self.con.db_pickle('l', 'add')
        self.assertEqual("Invalid use of the command please enter "
                         "'replace'/'add' and a filename", output)

    def test_f4(self):
        print("f4")
        output = self.con.db_pickle('l', 'test')
        self.assertEqual("Invalid command please use either 'replace' or "
                         "'add'", output)

    def test_f5(self):
        print("f5")
        output = self.con.db_pickle('l', '')
        self.assertEqual("Invalid use of the command", output)

    def test_f6(self):
        print("f6")
        output = self.con.db_pickle('l', 'add TestFileThatDoesntExist')
        self.assertEqual("File not found", output)

    def test_f7(self):
        print("f7")
        output = self.con.db_pickle('l', 'replace test')
        self.assertEqual("Data loaded from test.pickle Successfully", output)

    def test_f8(self):
        print("f8")
        output = self.con.db_pickle('l', 'add test')
        self.assertEqual("Data loaded from test.pickle Successfully", output)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    unittest.main()
