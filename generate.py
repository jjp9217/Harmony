#!/usr/bin/env python3
import csv

import sqlconnect

play_song_SQL = "INSERT INTO p320_19.listens(songid, username, datetime) VALUES (%s, %s, %s)"

register_SQL = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
               "values (%s, %s, %s, %s, %s, %s);"

conn = sqlconnect.connect()
cur = conn.cursor()


def generate_listens():
    return


def generate_users():
    file = open("Data/MOCK_DATA_users.csv")
    file.readline()
    parser = csv.reader(file)
    for user in parser:
        cur.execute(register_SQL, (user[4], user[5], user[3], user[0], user[1], user[2]))
        conn.commit()




if __name__ == "__main__":
    # generate_users()


