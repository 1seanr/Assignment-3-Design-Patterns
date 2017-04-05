from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    @abstractmethod
    def set(self):
        pass

    @abstractmethod
    def get(self):
        pass
