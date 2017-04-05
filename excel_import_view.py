import xlrd

from view import View


class ExcelView(View):

    def __init__(self):
        self.__file_path = ""
        self.__filename = ""
        self.__myList = []

    def set(self, filename=None, file_path=None):
        self.__file_path = file_path
        self.__filename = filename

    def calculate(self):
        self.__myList = []
        if self.__file_path == '':
            book = xlrd.open_workbook(self.__filename)
        else:
            book = xlrd.open_workbook(self.__file_path + "\\" +
                                      self.__filename)
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
