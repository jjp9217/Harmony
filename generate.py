#!/usr/bin/env python3
import csv
import random, calendar
import pandas as pd
import sqlconnect
import datetime

play_song_SQL = "INSERT INTO p320_19.listens(songid, username, datetime) VALUES (%s, %s, %s)"

register_SQL = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
               "values (%s, %s, %s, %s, %s, %s);"

get_users_sql = "select username from p320_19.\"user\""



conn = sqlconnect.connect()
cur = conn.cursor()


def generate_listens():
    cur.execute(get_users_sql)
    users = cur.fetchall()
    for x in range(1, 72001):
        user = random.choice(users)[0]
        song = random.randrange(1, 16740)
        date = random_date(weekend=False)
        cur.execute(play_song_SQL, (song, user, date))
        # print(f"{user} {song} {date}")
    conn.commit()


def generate_users():
    file = open("Data/MOCK_DATA_users.csv")
    file.readline()
    parser = csv.reader(file)
    for user in parser:
        cur.execute(register_SQL, (user[4], user[5], user[3], user[0], user[1], user[2]))
        conn.commit()


def generate_weekend_listens():
    cur.execute(get_users_sql)
    users = cur.fetchall()
    for x in range(1, 18001):
        user = random.choice(users)[0]
        song = random.randrange(1, 16740)
        date = random_date(weekend=True)
        cur.execute(play_song_SQL, (song, user, date))
        # print(f"{user} {song} {date}")
    conn.commit()



def random_date(weekend):
    # day_count = calendar.monthrange(year, month)[1]
    t = random.choice(pd.date_range(f"{2018}-{3}-01", f"{2022}-{3}-{31}", freq='D'))
    if weekend:
        if t.dayofweek == 5 or t.dayofweek == 6:
            return add_time(t)
        else:
            return random_date(weekend)
    else:
        return add_time(t)


def add_time(date):
    hours = random.randrange(0, 24)
    minutes = random.randrange(0, 60)
    sec = random.randrange(0, 60)
    return pd.Timestamp.combine(date, datetime.time(hours, minutes, sec))




if __name__ == "__main__":
    # generate_users()
    # d = random_date(weekend=True)
    # d = add_time(d)
    # d.combine(d,)
    # print(d)
    generate_weekend_listens()
    generate_listens()
    sqlconnect.disconnect(conn)

