from db_view import DBView


class GetDataFromDB(DBView):
    def get(self, selections, condition):
        if condition != "":
            condition = 'WHERE ' + condition
        self._cur.execute('SELECT ' + selections + ' FROM Employee ' +
                          condition)

        rows = self._cur.fetchall()
        self.close_connection()
        return rows
