import sqlite3
from sqlite3 import OperationalError, IntegrityError

from i_view import View


class DBView(View):

    def __init__(self):
        # Connecting to the database file
        self.__sqlite_file = 'employeeDb'    # name of the sqlite database file
        # Creates connection object
        self.__conn = sqlite3.connect(self.__sqlite_file)
        # creates curser object
        self.__cur = self.__conn.cursor()
        self.__recreate_db()
        self.__insert_start_data()

    def __recreate_db(self):
        self.__cur.execute("""DROP TABLE IF EXISTS employee;""")

        try:
            self.__cur.execute("SELECT count(*) FROM employeeDb WHERE type = "
                               "'table' AND name = 'Employee';")
        except OperationalError:
            self.__cur.execute('''CREATE TABLE IF NOT EXISTS Employee(
                EMPID    	VarChar(4) primary key,
                Gender	 	VarChar(1),
                Age      	int(2),
                Sales 		int(3),
                BMI         VarChar(11),
                Salary      int(3),
                Birthday    date);''')

    def __insert_start_data(self):
            self.__cur.execute('''insert into Employee values('T123', 'M', 20,
             654, 'Normal', 56, '1996-10-18');''')
            self.__cur.execute('''insert into Employee values('G834', 'M', 54,
            213, 'Overweight', 566, '1990-12-4');''')
            self.__cur.execute('''insert into Employee values('S931', 'F', 80,
            986, 'Obesity', 852, '2001-5-1');''')
            self.__cur.execute('''insert into Employee values('P912', 'M', 34,
            43, 'Underweight', 135, '1998-7-26');''')
            self.__cur.execute('''insert into Employee values('B720', 'F', 67,
            867, 'Normal', 741, '1993-1-6');''')

            print("Inserted Initial DB Entries")
            self.__conn.commit()

    def close_connection(self):
        self.__conn.close()

    def get(self, selections=None, condition=None):
        if condition != "":
            condition = 'WHERE ' + condition
        self.__cur.execute('SELECT ' + selections + ' FROM Employee ' +
                           condition)

        rows = self.__cur.fetchall()
        return rows

    def set(self, data_list=None, replace=None):
        if replace == 'R':
            self.__recreate_db()
        count = 1
        invalid_array = []
        for row in data_list:
            try:
                self.__cur.execute("insert into Employee values ('" + row[0] +
                                   "', '" + row[1] + "', " +
                                   str(int(row[2])) + ", " + str(int(row[3])) +
                                   ", '" + row[4] + "', " +
                                   str(int(row[5])) + ", '" + row[6] + "');")
                self.__conn.commit()
            except IntegrityError:
                invalid_array.append(count)
            finally:
                count += 1
        for item in invalid_array:
            print("Could not save data to the data base due to conflicting "
                  "primary keys or other compromised data\n" +
                  "On line " + str(item) + "\nAll other rows have been saved")
