from cmd import Cmd

from i_cview import CView


class CmdView(Cmd, CView):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.__con = None
        self.__latest_output = []

    def set_controller(self, controller):
        self.__con = controller

    def output(self, output):
        print(output)

    def output_list(self, output_list):
        for row in output_list:
            print(row)

    def do_load(self, line):
        """load [selections] [conditions]
        Brings the Data out of the database that matched the statements input
        If left blank will display all the employees in database
        For example to display just ID's of employees with age over 20
          input would be 'load EMPID Age>20'"""
        print(self.__con.load_from_db(line))

    def do_save(self, line):
        """save
        Saves the last data that has been Loaded out of Excel to the
        Database"""
        print(self.__con.save_to_db())

    def do_import(self, line):
        """import [filepath]\\[filename].xls
        For example:
          when making a list of directories put 2 back slashes between each
          directory
          If the file is in a folder called 'testingDir'
          and file is called 'TestFile' (type in xls extension as well)
          Applicable command would be 'TestingDir\\TestFile.xls'"""
        self.output_list(self.__con.import_from_excel(line))

    def do_validate(self, line):
        """validate
        Validates currently Loaded data
        Should be used after 'Load' and before 'Save'"""
        print(self.__con.validate_data())

    def do_view(self, line):
        """view
        Displays in list format data that has been brought in by 'Load'"""
        self.output_list(self.__con.view())

    def do_matplot(self, line):
        """matplot
        It plots out all of the ages of the Employees that are stored
        in the database
        """
        self.__con.matplot_data()

    def do_savedb(self, line):
        """savedb [filename]
        Used to back up the current Database to a .pickle file
        When saving will automatically add ".pickle" to the end of the filename
        e.g if the command 'savedb hello' was used it would have
        the db as hello.pickle"""
        print(self.__con.db_pickle('s', line))

    def do_loaddb(self, line):
        """loaddb (replace/add) [filename]
        Used to either replace the current database with a saved one
            This is done by using the 'replace' option
        Or add the data from a saved one to the current one
            This is done by using the 'add' option and any clashing data
                between the saved db and current db will just
            be left as is in the current live db and not overwritten by the
                clashing data in the saved one
        .pickle is automatically added to the end of the filename it is
            trying to load
        e.g. so if trying to load the file hello.pickle and add it to the
            current db it would be 'loaddb add hello'
        """
        print(self.__con.db_pickle('l', line))

    def do_quit(self, line):
        print("Bye")
        return True


