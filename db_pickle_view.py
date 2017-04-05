import pickle

from view import View


class DBPickleView(View):

    def __init__(self):
        self.__filename = ""
        self.__save_me = []

    def set(self, __filename=None, data_to_be_saved=None):
        self.__filename = __filename
        self.__save_me = data_to_be_saved

    def get(self):
        if self.__save_me is not None:
            with open((self.__filename + ".pickle"), 'wb') as f:
                pickle.dump(self.__save_me, f)
            return "Saved Successfully as: " + self.__filename + ".pickle"
        else:
            try:
                with open((self.__filename + ".pickle"), 'rb') as f:
                    return pickle.load(f)
            except FileNotFoundError:
                return "File not found"
