# going to create a class called DBHelper
import pymysql, dbconfig

class DBHelper:

    def connect(self, database="crimemap"):
        return pymysql.connect(host=dbconfig.host,
                                port=dbconfig.port,
                                user=dbconfig.db_user,
                                password=dbconfig.db_password,
                                db=database)
    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            # the following introduces a deliberate security flaw. sql injection
            query = "INSERT INTO crimes (description) VALUES (%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()



