import re
from datetime import date


class ValidateData:
    def __init__(self, data_list):
        self.__result_list = []
        self.__age = 0
        self.__regexp_list = ["^[A-Z][0-9]{3}$",
                              "(^(M|m)$|^(F|f)$|^(M|m)ale$|^(F|f)emale$)",
                              "^[0-9]{2}$", "^[0-9]{3}$",
                              "(^(N|n)ormal$|^(O|o)verweight$|^(O|o)bese"
                              "$|^(U|u)nderweight$)",
                              "^[0-9]{2,3}$", ""]
        self.__data_validation_handler(data_list)

    def __valid_bday_date_and_matching_age(self, day, month, year):
        try:
            birth_date = date(year, month, day)
            today = date.today()
            calculated_age = \
                today.year - birth_date.year - \
                ((today.month, today.day) < (birth_date.month, birth_date.day))
            if calculated_age == self.__age:
                is_valid = True
            else:
                is_valid = False
        except ValueError:
            is_valid = False
        return is_valid

    @staticmethod
    def __reg_exp_checker(regexp, string):
        if re.search(regexp, string):
            return True
        else:
            return False

    def __data_validation_handler(self, data_list):
        self.__result_list = []
        outer_list_pos = 0
        for row in data_list:
            temp_result_list = self.__search_through_data_and_build_results(
                row)
            self.__result_list.append(temp_result_list)
            outer_list_pos += 1

    def __search_through_data_and_build_results(self, row_of_data):
        temp_result_list = []
        inner_list_pos = 0
        try:
            for row_item in row_of_data:
                if row_item != "":
                    self.__sort_and_check_row_data(row_item, inner_list_pos,
                                                   temp_result_list)
                else:
                    temp_result_list.append(False)
                inner_list_pos += 1
        except IndexError:
            temp_result_list = (False, False, False, False, False,
                                False, False)
        return temp_result_list

    def __sort_and_check_row_data(self, row_item, inner_list_pos,
                                  temp_result_list):
        if inner_list_pos == 2:
            self.__age = int(float(row_item))

        if inner_list_pos == 6:
            self.__birth_date_check(row_item, temp_result_list)
            return

        elif isinstance(row_item, float):
            row_item = str(int(row_item))

        temp_result_list.append(self.__reg_exp_checker(
            self.__regexp_list[inner_list_pos], row_item))

    def __birth_date_check(self, col, temp_result_list):
        try:
            col = col.replace("/", "-").replace(" ", "-")
            try:
                day, month, year = col.split("-")
                temp_result_list.append(
                    self.__valid_bday_date_and_matching_age(int(float(day)),
                                                            int(float(month)),
                                                            int(float(year))))
            except ValueError:
                pass
            if len(temp_result_list) != len(self.__regexp_list):
                temp_result_list.append(False)
        except AttributeError:
            temp_result_list.append(False)

    def get_results(self):
        return self.__result_list
