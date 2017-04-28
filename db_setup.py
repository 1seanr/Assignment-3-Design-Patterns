from sqlite3 import OperationalError

from db_view import DBView


class DBSetup(DBView):
    def __init__(self):
        super().__init__()
        self.__recreate_db()
        self.__insert_start_data()
        self.close_connection()

    def __recreate_db(self):
        self._cur.execute("""DROP TABLE IF EXISTS employee;""")

        try:
            self._cur.execute("SELECT count(*) FROM employeeDb WHERE type = "
                              "'table' AND name = 'Employee';")
        except OperationalError:
            self._cur.execute('''CREATE TABLE IF NOT EXISTS Employee(
                EMPID    	VarChar(4) primary key,
                Gender	 	VarChar(1),
                Age      	int(2),
                Sales 		int(3),
                BMI         VarChar(11),
                Salary      int(3),
                Birthday    date);''')

    def __insert_start_data(self):
        self._cur.execute('''insert into Employee values('T123', 'M', 20,
             654, 'Normal', 56, '1996-10-18');''')
        self._cur.execute('''insert into Employee values('G834', 'M', 54,
            213, 'Overweight', 566, '1990-12-4');''')
        self._cur.execute('''insert into Employee values('S931', 'F', 80,
            986, 'Obesity', 852, '2001-5-1');''')
        self._cur.execute('''insert into Employee values('P912', 'M', 34,
            43, 'Underweight', 135, '1998-7-26');''')
        self._cur.execute('''insert into Employee values('B720', 'F', 67,
            867, 'Normal', 741, '1993-1-6');''')

        print("Inserted Initial DB Entries")
        self._conn.commit()
