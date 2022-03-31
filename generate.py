#!/usr/bin/env python3
import sqlconnect

play_song_SQL = "INSERT INTO p320_19.listens(songid, username, datetime) VALUES (%s, %s, %s)"

register_SQL = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
               "values (%s, %s, %s, %s, %s, %s);"

conn = sqlconnect.connect()
cur = conn.cursor()


def generate_listens():
    return

def generate_users():


if __name__ == "__main__":
