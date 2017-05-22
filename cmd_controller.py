from sqlite3 import OperationalError
from db_setup import DBSetup
from db_setting_getting_data_view import SetAndGetDataFromDB

from validating_input import ValidateData


class CmdController(object):

    def __init__(self, cmd_view, excel_view, mp_view, db_p_view):
        DBSetup()
        self.__cmd_view = cmd_view
        self.__excel_view = excel_view
        self.__mp_view = mp_view
        self.__db_pic_view = db_p_view
        self.__imported_data_list = []
        self.__validation_flag = False

    def go(self, controller):
        self.__cmd_view.set_controller(controller)
        from sys import argv
        if len(argv) > 1:
            self.__cmd_view.onecmd(' '.join(argv[1:]))
        self.__cmd_view.cmdloop()

    def load_from_db(self, line):
        get_data = SetAndGetDataFromDB()
        try:
            if line != "":
                selections, conditions = line.split(" ")
            else:
                selections = "*"
                conditions = ""
            return get_data.get(selections, conditions)
        except (ValueError, OperationalError):
            return "Invalid use of the command"

    def save_to_db(self):
        if self.__validation_flag:
            set_data = SetAndGetDataFromDB()
            set_data.set(self.__imported_data_list)
            return "Saved successfully"
        else:
            return "Please validate the data using the 'validate' command"

    def import_from_excel(self, input_str):
        if input_str.endswith(".xls"):
            try:
                self.__excel_view.set(input_str)
                self.__excel_view.calculate()
                self.__imported_data_list = self.__excel_view.get()
                self.__validation_flag = False
                self.__cmd_view.output("The data imported is:")
                return self.__imported_data_list
            except FileNotFoundError:
                return ["That file or directory does not exist"]
        else:
            return ["Invalid use of the command"]

    def validate_data(self):
        is_all_data_valid = True
        validate_object = ValidateData(self.__imported_data_list)
        row_count = 1
        invalid_rows = ""
        for row_of_data in validate_object.get_results():
            stopping_duplicate_rows_flag = True
            for row_item in row_of_data:
                if not row_item:
                    if stopping_duplicate_rows_flag:
                        stopping_duplicate_rows_flag = False
                        is_all_data_valid = False
                        invalid_rows += str(row_count) + " "
            row_count += 1

        if is_all_data_valid:
            self.__validation_flag = True
            return "Data is valid you can now save"
        else:
            return "Data not valid please correct it\n Invalid data on rows: "\
                   + invalid_rows

    def view_currently_stored_import_data(self):
        return self.__imported_data_list

    def matplot_data(self):
        get_data_from_db = SetAndGetDataFromDB()
        self.__mp_view.display(get_data_from_db.get("*", ""))

    def db_pickle(self, sav_or_loa_from_db, input_command_param):
        if input_command_param == "":
            return "Invalid use of the command"

        if sav_or_loa_from_db == 's':
            get_data_from_db = SetAndGetDataFromDB()
            self.__db_pic_view.set([input_command_param,
                                    get_data_from_db.get('*', '')])
            return self.__db_pic_view.get()

        else:
            set_data = SetAndGetDataFromDB()
            array_of_input = input_command_param.split(' ')
            try:
                if array_of_input[0] == "replace" or array_of_input[0] == \
                        "add":
                    self.__db_pic_view.set([array_of_input[1], None])
                else:
                    return "Invalid command please use either 'replace' or " \
                           "'add'"
            except IndexError:
                return "Invalid use of the command please enter " \
                       "'replace'/'add' and a filename"

            loaded_data = self.__db_pic_view.get()

            if not loaded_data[0]:
                return ['File not found']

            if array_of_input[0] == "replace":
                replace_loaded_data = [loaded_data, 'R']
                set_data.set(replace_loaded_data)

            if array_of_input[0] == "add":
                set_data.set(loaded_data)
            return "Data loaded from " + array_of_input[1] + \
                   ".pickle Successfully"
