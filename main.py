from cmd_controller import CmdController
from cmd_view import CmdView
from db_pickle_view import DBPickleView
from excel_import_view import ExcelView
from matplot_view import MatPlotView

if __name__ == '__main__':
    controller = CmdController(CmdView(), ExcelView(), MatPlotView(),
                               DBPickleView())
    controller.go(controller)
