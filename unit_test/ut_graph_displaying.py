import unittest

from cmd_controller import CmdController
from cmd_view import CmdView
from db_pickle_view import DBPickleView
from excel_import_view import ExcelView
from matplot_view import MatPlotView
from db_view import DBView


class GraphingTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.con = CmdController(CmdView(), ExcelView(), DBView(),
                                 MatPlotView(), DBPickleView())

    def tearDown(self):
        # be executed after each test case
        print('End of Test\n\n')

    def test_PlotBaseData(self):
        self.con.matplot_data()

    def test_ImportDataThenPlot(self):
        self.con.import_from_excel("TestingDir\FullRangeValidTestFile.xls")
        self.con.validate_data()
        self.con.save_to_db()
        self.con.matplot_data()
