#!/usr/bin/env python3
# music.csv format
# "artist.familiarity","artist.hotttnesss","artist.id","artist.latitude","artist.location","artist.longitude","artist.name","artist.similar","artist.terms","artist.terms_freq","release.id","release.name","song.artist_mbtags","song.artist_mbtags_count","song.bars_confidence","song.bars_start","song.beats_confidence","song.beats_start","song.duration","song.end_of_fade_in","song.hotttnesss","song.id","song.key","song.key_confidence","song.loudness","song.mode","song.mode_confidence","song.start_of_fade_out","song.tatums_confidence","song.tatums_start","song.tempo","song.time_signature","song.time_signature_confidence","song.title","song.year"
import sqlconnect
import psycopg2

artist_name_idx = 6
song_duration_idx = 18
song_title_idx = 33
song_year = 34


def get_indexes():
    file = open("music.csv")
    indexes = file.readline().split(",")
    i = 0
    for idx in indexes:
        print(i, idx)
        i += 1
    file.close()


if __name__ == "__main__":
    file = open("music.csv")
    file.readline()
    conn = sqlconnect.connect()
    cur = conn.cursor()

    # for line in file:
    #     line = line.split(",")
    #     print(line[artist_name_idx], line[song_duration_idx])
        # cur.execute(f"INSERT INTO p320_19.artists(artistid, artist_name) Values (1,'{line[artist_name_idx]}');")

    # cur.execute("INSERT INTO p320_19.artists(artistid, artist_name) Values (3,'testing');")

    cur.execute("SELECT * FROM p320_19.artists")
    print(cur.)


    file.close()
