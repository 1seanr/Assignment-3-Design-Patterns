from abc import ABCMeta, abstractmethod


class CView(metaclass=ABCMeta):
    @abstractmethod
    def set_controller(self, output):
        pass

    @abstractmethod
    def output(self, output):
        pass

    @abstractmethod
    def output_list(self, output_list):
        pass

    @abstractmethod
    def set_controller(self, controller):
        pass

    @abstractmethod
    def do_load(self, line):
        pass

    @abstractmethod
    def do_save(self, line):
        pass

    @abstractmethod
    def do_import(self, line):
        pass

    @abstractmethod
    def do_validate(self, line):
        pass

    @abstractmethod
    def do_view(self, line):
        pass

    @abstractmethod
    def do_matplot(self, line):
        pass

    @abstractmethod
    def do_savedb(self, line):
        pass

    @abstractmethod
    def do_loaddb(self, line):
        pass

    @abstractmethod
    def do_quit(self, line):
        pass
