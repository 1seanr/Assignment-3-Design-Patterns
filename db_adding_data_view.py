from db_view import DBView
from db_setup import DBSetup
from sqlite3 import IntegrityError


class AddDataToDB(DBView):
    def set(self, data_list):
        if len(data_list) == 2:
            if data_list[1] == 'R':
                DBSetup()
                data_list = data_list[0]
        count = 1
        invalid_array = []
        for row in data_list:
            try:
                self._cur.execute("insert into Employee values ('" + row[0] +
                                  "', '" + row[1] + "', " +
                                  str(int(row[2])) + ", " + str(int(row[3])) +
                                  ", '" + row[4] + "', " +
                                  str(int(row[5])) + ", '" + row[6] + "');")
                self._conn.commit()
            except IntegrityError:
                invalid_array.append(count)
            finally:
                count += 1
        for item in invalid_array:
            print("Could not save data to the data base due to conflicting "
                  "primary keys or other compromised data\n" +
                  "On line " + str(item) + "\nAll other rows have been saved")
        self.close_connection()
