from sqlite3 import OperationalError

from validating_input import ValidateData


class CmdController(object):

    def __init__(self, cmd_view, excel_view, db_view, mp_view, db_p_view):
        self.__cmd_view = cmd_view
        self.__excel_view = excel_view
        self.__db_view = db_view
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
        try:
            if line != "":
                selections, conditions = line.split(" ")
            else:
                selections = "*"
                conditions = ""
            return self.__db_view.get(selections, conditions)
        except (ValueError, OperationalError):
            return "Invalid use of the command"

    def save_to_db(self):
        if self.__validation_flag:
            self.__db_view.set(self.__imported_data_list)
            return "Saved successfully"
        else:
            return "Please validate the data using the 'validate' command"

    def import_from_excel(self, input_str):
        file_address = input_str.rsplit('\\', 1)
        if len(file_address) == 1 and file_address[0].endswith(".xls"):
            file_address.append("")
            file_address[1] = file_address[0]
            file_address[0] = ""
        if len(file_address) == 2:
            try:
                self.__excel_view.set(file_address[1], file_address[0])
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
        flag = True
        validate_object = ValidateData(self.__imported_data_list)
        count = 1
        invalid_rows = ""
        for i in validate_object.get_results():
            per_row_flag = True
            for j in i:
                if not j:
                    if per_row_flag:
                        per_row_flag = False
                        flag = False
                        invalid_rows += str(count) + " "
            count += 1

        if flag:
            self.__validation_flag = True
            return "Data is valid you can now save"
        else:
            return "Data not valid please correct it\n Invalid data on rows: "\
                   + invalid_rows

    def view(self):
        return self.__imported_data_list

    def matplot_data(self):
        # passes the db data to the matplot view
        self.__mp_view.set(self.__db_view.get("*", ""))
        self.__mp_view.get()

    def db_pickle(self, sav_or_loa, line):
        # makes sure they input a parameter
        if line == "":
            return "Invalid use of the command"
        # Saving to a pickle file
        if sav_or_loa == 's':
            self.__db_pic_view.set(line, self.__db_view.get('*', ''))
            return self.__db_pic_view.get()
        # Loading from a pickle file
        elif sav_or_loa == 'l':
            array_of_input = line.split(' ')
            try:
                if array_of_input[0] == "replace" or array_of_input[0] == \
                        "add":
                    self.__db_pic_view.set(array_of_input[1])
                else:
                    return "Invalid command please use either 'replace' or " \
                           "'add'"
            except IndexError:
                return "Invalid use of the command please enter " \
                       "'replace'/'add' and a filename"

            loaded_data = self.__db_pic_view.get()

            # If it couldn't find the file it will return an error message
            # here and stop
            if isinstance(loaded_data, str):
                return loaded_data

            # When replacing current DB
            if array_of_input[0] == "replace":
                self.__db_view.set(loaded_data, 'R')
            # When adding to the current DB
            elif array_of_input[0] == "add":
                self.__db_view.set(loaded_data)
            return "Data loaded from " + array_of_input[1] + \
                   ".pickle Successfully"
