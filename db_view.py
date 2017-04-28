import sqlite3


class DBView(object):
    def __init__(self):
        # Connecting to the database file
        self.__sqlite_file = 'employeeDb'    # name of the sqlite database file
        # Creates connection object
        self._conn = sqlite3.connect(self.__sqlite_file)
        # creates curser object
        self._cur = self._conn.cursor()

    def close_connection(self):
        self._conn.close()
