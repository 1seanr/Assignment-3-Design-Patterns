import xlrd

from i_view import View


class ExcelView(View):

    def __init__(self):
        self.__file_path_and_filename = ""
        self.__myList = []

    def set(self, file_path_and_filename):
        self.__file_path_and_filename = file_path_and_filename

    def calculate(self):
        self.__myList = []
        book = xlrd.open_workbook(self.__file_path_and_filename)
        sh = book.sheet_by_index(0)
        # my testing
        for rx in range(sh.nrows):
            temp_list = []
            for cy in range(sh.ncols):
                temp_list.append(sh.cell_value(rowx=rx, colx=cy))
            self.__myList.append(temp_list)

    # print(myList)
    def get(self):
        return self.__myList
