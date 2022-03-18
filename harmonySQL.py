"""
@author Jesse Pingitore
file: harmonySQL.py
This file acts as a utility dump for the SQL calls.
It holds both the string templates for the calls, and functions for different user actions.
"""
import datetime

import sqlconnect

"""
    Constants
"""
register_sql = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
      "values (%s, %s, %s, %s, %s, %s);"

user_exists_sql = "select * from p320_19.\"user\" where username = '%s'"

login_SQL = "select * from p320_19.\"user\" where username = '%s' and password = '%s';"



# insert into p320_19."user" (username, acc_creation_date, password, first_name, last_name, email)
# values ('test', '2022-03-17', 'pass', 'catherine', 'katherine', 'null@gmail.com');
import sqlconnect

register_SQL = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
      "values (%s, %s, %s, %s, %s, %s);"

# TODO
search_user_SQL = "SELECT * FROM p320_19.dummy;"



def register():

        # First, open a database connection
        connection = sqlconnect.connect()

        # Create a cursor. It allows us to execute SQL commands.
        cursor = connection.cursor()

        ### Build the user input

        username = input("provide a new username: >")

        #TODO Select the DB to find if this username is taken

        password = input("provide a new password: >")
        email = input("provide an email address: >")
        f_name = input("first name: >")
        l_name = input("last name: >")
        current_date = str(datetime.date.today()) #cast date to yyyy-mm-dd string


        # Now try to add this person to the DB.
        cursor.execute(register_sql, (username, current_date, password,  f_name, l_name, email ))

        # Make the change
        connection.commit()

        # Terminate connection
        sqlconnect.disconnect(connection)


if __name__ == "__main__":
        register()
