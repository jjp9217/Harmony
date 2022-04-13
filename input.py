#!/usr/bin/env python3
import datetime
import sqlconnect
import csv

artist_name_idx = 2
song_duration_idx = 18
song_title_idx = 1
song_year = 3
album_name = 3
genre_idx = 4


def get_indexes():
    file = open("Data/music.csv")
    indexes = file.readline().split(",")
    i = 0
    for idx in indexes:
        print(i, idx)
        i += 1
    file.close()


def input_albums():
    albums = open("Data/album names.txt", newline='')
    albums.readline()
    dates = open("Data/MOCK_DATA.csv", newline='')
    dates.readline()
    parser = csv.reader(albums)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1
    cur.execute("DELETE FROM p320_19.albums;")
    conn.commit()
    for line in parser:
        date = dates.readline()
        name = line[album_name][2:-1].replace("'", "''")
        cur.execute(f"INSERT INTO p320_19.albums(albumid, release_date, name) Values ({i},'{date}','{name}');")

        i += 1
        conn.commit()
        if i > 1000:
            break

    cur.execute("SELECT * FROM p320_19.artists")

    sqlconnect.disconnect(conn)
    albums.close()
    dates.close()


def input_artists():
    file = open("Data/top1000.txt", newline='')
    file.readline()
    parser = csv.reader(file)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1
    cur.execute("DELETE FROM p320_19.artists;")
    conn.commit()
    for line in parser:
        query = f"INSERT INTO p320_19.artists(artistid, artist_name) Values ({i},'{line[artist_name_idx]}');"
        try:
            cur.execute(query)
            i += 1
        except Exception as e:
            print(e)
            print(query)
        finally:
            conn.commit()

    sqlconnect.disconnect(conn)
    file.close()


def input_songs():
    songs = open("Data/top1000.txt", newline='')
    songs.readline()
    dates = open("Data/MOCK_DATA.csv", newline='')
    dates.readline()
    durations = open("Data/music.csv", newline='')
    durations.readline()
    dur_parser = csv.reader(durations)
    parser = csv.reader(songs)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1
    cur.execute("DELETE FROM p320_19.songs;")
    conn.commit()
    durs = []
    for line in dur_parser:
        dur = str(datetime.timedelta(seconds=float(line[song_duration_idx])))
        durs.append(dur)

    for line in parser:
        date = dates.readline()

        name = line[song_title_idx].replace("'", "''")
        cur.execute(f"INSERT INTO p320_19.songs(songid, release_date, name, duration) Values ({i},'{date}','{name}','{durs[i]}');")

        i += 1
        conn.commit()
        if i > 1000:
            break


    sqlconnect.disconnect(conn)
    dates.close()
    songs.close()
    durations.close()


def input_more_songs():
    songs = open("music_data.txt", newline='')
    songs.readline()
    s_parser = csv.reader(songs, delimiter=',')
    conn = sqlconnect.connect()
    cur = conn.cursor()
    conn.commit()
    for line in s_parser:
        i = int(line[3])
        time = convert(i)
        try:
            query = """INSERT INTO p320_19.songs (songid, 
            release_date, name, duration) 
            VALUES (%s, %s, %s, %s)"""
            tuple = (line[0], line[1], line[2], time)
            cur.execute(query, tuple)
            print("Data inserted successfully into the songs table using "
                  "the prepared statement")
        except Exception as e:
            print(e)
        finally:
            conn.commit()
    songs.close()


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


def input_genre():
    file = open("Data/Genres.txt", newline='')
    file.readline()
    parser = csv.reader(file)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM p320_19.genres;")
    conn.commit()
    for line in parser:
        try:
            cur.execute(f"INSERT INTO p320_19.genres( name) Values ('{line[0]}');")
        except Exception as e:
            print(e)
        finally:
            conn.commit()

    sqlconnect.disconnect(conn)
    file.close()


def input_song_artist():
    file = open("Data/MOCK_DATA_artist_song.csv", newline='')

    file.readline()
    parser = csv.reader(file)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1

    cur.execute("DELETE FROM p320_19.artist_song_production;")
    conn.commit()
    for line in parser:
        cur.execute(f"INSERT INTO p320_19.artist_song_production(songid, artistid) Values ({i},{line[0]});")
        i += 1
        conn.commit()

    sqlconnect.disconnect(conn)
    file.close()


def input_song_genre():
    file = open("Data/MOCK_DATA_Song_genres.csv", newline='')
    file.readline()
    parser = csv.reader(file)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1
    cur.execute("DELETE FROM p320_19.song_genre;")
    conn.commit()
    for line in parser:
        cur.execute(f"INSERT INTO p320_19.song_genre(songid, genreid) Values ({i},{line[0]});")
        i += 1
        conn.commit()

    sqlconnect.disconnect(conn)
    file.close()


def input_song_album():
    file = open("Data/MOCK_DATA_song_albums.csv", newline='')
    file.readline()
    parser = csv.reader(file)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1
    cur.execute("DELETE FROM p320_19.collected_songs;")
    conn.commit()
    for line in parser:
        cur.execute(f"INSERT INTO p320_19.collected_songs(songid, albumid,track_number) Values ({i},{line[0]},{line[1]});")
        i += 1
        conn.commit()

    sqlconnect.disconnect(conn)
    file.close()



def input_album_genre():
    file = open("Data/MOCK_DATA_album_genres.csv", newline='')
    file.readline()
    parser = csv.reader(file)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1
    cur.execute("DELETE FROM p320_19.album_genre;")
    conn.commit()
    for line in parser:
        cur.execute(f"INSERT INTO p320_19.album_genre(albumid,genreid) Values ({i},{line[0]});")
        i += 1
        conn.commit()

    sqlconnect.disconnect(conn)
    file.close()


def input_album_artist():
    file = open("Data/MOCK_DATA_album_artist.csv", newline='')
    file.readline()
    parser = csv.reader(file)
    conn = sqlconnect.connect()
    cur = conn.cursor()
    i = 1
    cur.execute("DELETE FROM p320_19.artist_album_production;")
    conn.commit()
    for line in parser:
        cur.execute(f"INSERT INTO p320_19.artist_album_production(albumid,artistid) Values ({i},{line[0]});")
        i += 1
        conn.commit()

    sqlconnect.disconnect(conn)
    file.close()


if __name__ == "__main__":
    # probably best to not run all of these at once since they will remove all the data and repopulate the database
    # this takes a bit to do all at once
    # input_album_artist()
    input_album_genre()
    # input_genre()
    # input_song_genre()
    # input_album_genre()
    # input_song_album()
    # input_artists()
    # input_more_songs()
    # input_songs()
    # input_artists()
    # input_albums()

