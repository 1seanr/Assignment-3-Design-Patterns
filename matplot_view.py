import matplotlib.pyplot as plt

from i_view import View


class MatPlotView(View):
    def __init__(self):
        self.__input_data_list = []

    def set(self, input_data_list=None):
        for i in input_data_list:
            self.__input_data_list.append(i[2])

    def get(self):
        bins = range(0, 100, 5)
        plt.hist(self.__input_data_list, bins, histtype='bar', rwidth=0.9)

        plt.ylabel('Number of Employees')
        plt.xlabel('Ages')
        plt.title('Employee Ages')
        plt.show()
