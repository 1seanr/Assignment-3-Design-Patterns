import re
from datetime import date


class ValidateData:
    def __init__(self, data_list):
        self.__result_list = []
        self.__age = 0
        self.__data_validation_handler(data_list)

    def __date_check(self, day, month, year):
        try:
            birth_date = date(year, month, day)
            today = date.today()
            calculated_age = \
                today.year - birth_date.year - \
                ((today.month, today.day) < (birth_date.month, birth_date.day))
            if calculated_age == self.__age:
                if (today.year - birth_date.year) >= 0:
                    is_valid = True
                else:
                    is_valid = False
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
        regexp_list = ["^[A-Z][0-9]{3}$",
                       "(^(M|m)$|^(F|f)$|^(M|m)ale$|^(F|f)emale$)",
                       "^[0-9]{2}$", "^[0-9]{3}$",
                       "(^(N|n)ormal$|^(O|o)verweight$|^(O|o)bese$|^("
                       "U|u)nderweight$)",
                       "^[0-9]{2,3}$", ""]
        outer_list_pos = 0
        for row in data_list:
            temp_result_list = []
            inner_list_pos = 0
            try:
                # Going through all of the items in each row
                for col in row:
                    if col != "":
                        if inner_list_pos == 2:
                            self.__age = int(float(col))
                        # This is to check the birth date using date check method
                        if inner_list_pos == 6:
                            try:
                                col = col.replace("/", "-").replace(" ", "-")
                                try:
                                    day, month, year = col.split("-")
                                    temp_result_list.append(
                                        self.__date_check(int(float(day)),
                                                          int(float(month)),
                                                          int(float(year))))
                                except ValueError:
                                    pass
                                if len(temp_result_list) != len(regexp_list):
                                    temp_result_list.append(False)
                            except AttributeError:
                                temp_result_list.append(False)
                        # If its not the birth date its checking it uses the regex
                        # checking method
                        elif isinstance(col, float):
                            temp_result_list.append(self.__reg_exp_checker(
                                regexp_list[inner_list_pos], str(int(col))))
                        else:
                            temp_result_list.append(self.__reg_exp_checker(
                                regexp_list[inner_list_pos], col))
                    else:
                        temp_result_list.append(False)
                    inner_list_pos += 1
            except IndexError:
                temp_result_list = (False, False, False, False, False,
                                    False, False)
            self.__result_list.append(temp_result_list)
            outer_list_pos += 1

    def get_results(self):
        return self.__result_list
