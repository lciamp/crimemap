# going to create a class called DBHelper
import datetime, dbconfig, pymysql

class DBHelper:
    """DBHelper class used for interacting with the database

    methods:
    connect         connects to the database
    get_all_inputs  returns all descriptions from database
    add_input       inserts description into database
    clear_all       deletes all from database
    add_crime       inserts whole crime into database
    """
    # connect to DB
    def connect(self, database="crimemap"):
        try:
            return pymysql.connect(host=dbconfig.host,
                                    port=dbconfig.port,
                                    user=dbconfig.db_user,
                                    password=dbconfig.db_password,
                                    db=database)
        except Exception as e:
            print e
    
    # get all crimes
    def get_all_crimes(self):
        connection = self.connect()
        try:
            query = "SELECT latitude, longitude, date, category, description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            named_crimes = []
            for crime in cursor:
                named_crime = {
                    'latitude': crime[0],
                    'longitude': crime[1],
                    'date': datetime.datetime.strftime(crime[2], '%m-%d-%Y'),
                    'category': crime[3],
                    'description': crime[4]
                }
                named_crimes.append(named_crime)
            return named_crimes
        except Exception as e:
            print e
        finally:
            connection.close()

    # add a crime definition
    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES (%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        except Exception as e:
            print e
        finally:
            connection.close()

    # delete all crimes
    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        except Exception as e:
            print e
        finally:
            connection.close()

    # add a crime
    def add_crime(self, category, date, latitude, longitude, description):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (category, date, latitude, longitude, description) VALUES (%s, %s, %s, %s, %s);"
            with connection.cursor() as cursor:
                cursor.execute(query, (category, date, latitude, longitude, description))
                connection.commit()
        except Exception as e:
            print e
        finally:
            connection.close()














