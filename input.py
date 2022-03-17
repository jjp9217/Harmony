#!/usr/bin/env python3
import sqlconnect
import re
import csv

artist_name_idx = 2
song_duration_idx = 18
song_title_idx = 1
song_year = 3
pattern = '(?:^|,)(?=[^"]|(")?)"?((?(1)[^"]*|[^,"]*))"?(?=,|$)'


def get_indexes():
    file = open("music.csv")
    indexes = file.readline().split(",")
    i = 0
    for idx in indexes:
        print(i, idx)
        i += 1
    file.close()


if __name__ == "__main__":
    file = open("top1000.txt", newline='')
    file.readline()
    parser = csv.reader(file)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1
    cur.execute("DELETE FROM p320_19.artists;")
    conn.commit()
    for line in parser:
        cur.execute(f"INSERT INTO p320_19.artists(artistid, artist_name) Values ({i},'{line[artist_name_idx]}');")
        i += 1
        conn.commit()


    # for line in file:
    #     # line = line.split(",")
    #     # artist_name_idx_temp = artist_name_idx
    #     # if line[1][0] == '"' and line[2][-1] != '"':
    #     #     while line[i][-1] != '"':
    #     #         artist_name_idx_temp += 1
    #     #     artist_name_idx_temp = i
    #     # result = re.match(pattern, line)
    #     #
    #     # print(result[1])
    #
    #
    #
    #     # cur.execute(f"INSERT INTO p320_19.artists(artistid, artist_name) Values ({i},'{result[artist_name_idx]}');")
    #     i += 1
    #     conn.commit()


    # cur.execute("INSERT INTO p320_19.artists(artistid, artist_name) Values (4,'testing');")


    cur.execute("SELECT * FROM p320_19.artists")
    print(cur.fetchall())

    sqlconnect.disconnect(conn)
    file.close()
