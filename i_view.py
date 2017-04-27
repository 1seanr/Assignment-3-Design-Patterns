from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    @abstractmethod
    def set(self, data_needed):
        pass

    @abstractmethod
    def get(self):
        pass
