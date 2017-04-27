import matplotlib.pyplot as plt


class MatPlotView(object):
    def __init__(self):
        self.__input_data_list = []

    def display(self, input_data_list):
        for i in input_data_list:
            self.__input_data_list.append(i[2])

        bins = range(0, 100, 5)
        plt.hist(self.__input_data_list, bins, histtype='bar', rwidth=0.9)

        plt.ylabel('Number of Employees')
        plt.xlabel('Ages')
        plt.title('Employee Ages')
        plt.show()
