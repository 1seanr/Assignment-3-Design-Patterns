import pickle

from i_view import View


class DBPickleView(View):

    def __init__(self):
        self.__filename = ""
        self.__save_me = []

    def set(self, filename_and_data):
        self.__filename = filename_and_data[0]
        self.__save_me = filename_and_data[1]

    def get(self):
        if self.__save_me is not None:
            with open((self.__filename + ".pickle"), 'wb') as f:
                pickle.dump(self.__save_me, f)
            return ["Saved Successfully as: " + self.__filename + ".pickle"]
        else:
            try:
                with open((self.__filename + ".pickle"), 'rb') as f:
                    return pickle.load(f)
            except FileNotFoundError:
                return [False]
