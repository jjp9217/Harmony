"""
@author Jesse Pingitore
file: harmonySQL.py
This file acts as a utility dump for the SQL call.
It holds both the string templates for the calls, and functions for different user actions.
Note that the actions here are ONLY for user interactions.
Any developer tools should use a different file.
"""
from cgi import print_environ
import datetime

import sqlconnect

"""
    Constants -----------------------------------------------------------------
"""

welcome_banner = "\n////// Welcome to Harmony \\\\\\\\\\\\"

register_sql = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
               "values (%s, %s, %s, %s, %s, %s);"

user_exists_sql = "select * from p320_19.\"user\" where username = %s"

email_exists_sql = "select * from p320_19.\"user\" where email = %s"

login_SQL = "select * from p320_19.\"user\" where username = %s and password = %s;"

register_SQL = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
               "values (%s, %s, %s, %s, %s, %s);"

create_playlist_SQL = "INSERT INTO p320_19.playlists(name, username) Values (%s, %s);"

# TODO
search_user_SQL = "SELECT * FROM p320_19.dummy;"

user_login_check_sql = "select * from p320_19.\"user\" where username = %s and password = %s;"

show_friends_sql = "select following_username FROM p320_19.following where follower_username = %s";

show_playlists_sql = "select playlistid, name FROM p320_19.playlists where username = %s order by name asc"

add_song_playlist_SQL = "INSERT INTO p320_19.collection_songs(playlistid, songid) Values (%s,%s);"

# check if playlist belongs to user
user_playlistid_check_sql = "select playlistid FROM p320_19.playlists where username = %s"

change_playlist_name_SQL = "Update p320_19.playlists SET name=%s WHERE playlistid=%s"

play_song_SQL = "INSERT INTO p320_19.listens(songid, username, datetime) VALUES (%s, %s, %s)"

select_songs_in_playlist = "SELECT songid from p320_19.collection_songs WHERE playlistid=%s;"

select_albums_in_playlist = "SELECT \"albumID\" from p320_19.collection_albums WHERE playlistid=%s;"

delete_playlist_sql = "Delete from p320_19.playlists where playlistid=%s"

delete_song_with_playlist = "Delete from p320_19.collection_songs where playlistid=%s"

delete_album_with_playlist = "Delete from p320_19.collection_albums where playlistid=%s"

add_song_playlist_SQL = "INSERT INTO p320_19.collection_songs(playlistid, songid) Values (%s,%s);"

add_album_playlist_SQL = "INSERT INTO p320_19.collection_albums(playlistid, \"albumID\") Values (%s,%s);"

delete_playlist_song_sql = "DELETE from p320_19.collection_songs where playlistid=%s and songid=%s";

delete_playlist_album_sql = "DELETE from p320_19.collection_albums where playlistid=%s and \"albumID\"=%s";

make_access_timestamp_sql = "insert into p320_19.access_timestamps(timestampid, username, datetime) " \
                            "values (default,%s,%s);"

"""
    Global Variables
"""
CONNECTION = sqlconnect.connect()
CURSOR = CONNECTION.cursor()

global USERNAME

"""
    User action functions -----------------------------------------------------
"""

"""
    User registration function.
    Creates a new user and adds it to the DB. Does check if name is taken to prevent crashing.
"""


def register():
    ### Build the user input
    username = input("Provide a new username: >")

    # Make sure the username is unique -- it is the key for the "users" table
    while True:

        CURSOR.execute(user_exists_sql, (
        username,))  # Note that even single arguments must be tuple-wrapped
        entries = CURSOR.fetchall()
        if len(entries) > 0:
            print("The username '" + username + "' is taken")
            username = input("Provide a new username: >")
            continue
        else:
            break

    password = input("Provide a new password: >")
    f_name = input("First name: >")
    l_name = input("Last name: >")
    current_date = str(
        datetime.date.today())  # cast date to yyyy-mm-dd string

    email = input("Provide an email address: >")

    # Make sure the email is unique -- which is part of project requirements
    while True:

        CURSOR.execute(email_exists_sql, (
        email,))  # Note that even single arguments must be tuple-wrapped
        entries = CURSOR.fetchall()
        if len(entries) > 0:
            print(
                "The username '" + email + "' is already in use with an account")
            email = input("Provide a different email: >")
            continue
        else:
            break

    # Now try to add this person to the DB.
    CURSOR.execute(register_sql, (
    username, current_date, password, f_name, l_name, email))

    # Make the change
    CONNECTION.commit()
    global USERNAME
    USERNAME = username

    # Print welcome banner
    print(welcome_banner)  # TODO ALSO USE AN ACCESS TIMESTAMP


"""
    Log the user in.
    Check if the supplied username/password combo exists in the DB.
"""


def login():
    username = input("Enter username: >")
    password = input("Enter password: >")

    while True:
        CURSOR.execute(login_SQL, (username, password))
        entries = CURSOR.fetchall()
        if len(entries) > 0:
            print("Logged in as user '" + username + "'")
            print(welcome_banner)
            break

        else:
            print("Username or Password are misspelled, or do not match")
            username = input("Enter username: >")
            password = input("Enter password: >")

    global USERNAME
    USERNAME = username

    CURSOR.execute(make_access_timestamp_sql,
                   (username, datetime.date.today()))
    CONNECTION.commit()


# finished Justin
def logout():
    sqlconnect.disconnect(CONNECTION)
    print("logged out\nGOODBYE")


# TODO Satvik
def search_name(songname):
    try:
        CURSOR.execute("SELECT * FROM p320_19.songs WHERE name=%s",
                       songname)

        rows = CURSOR.fetchall()

        for row in rows:
            print("Song: ", row[2], "Release Date: ", row[1], "Duration: ",
                  row[3])
            CURSOR.execute("SELECT * FROM p320_19.albums WHERE albumid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Album: ", r[2], "Release Date: ", r[1])

            CURSOR.execute("SELECT * FROM p320_19.artists WHERE "
                           "artistid=%s", (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Artist: ", r[1])

            CURSOR.execute("SELECT * FROM p320_19.genre WHERE genreid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Genre: ", r[1])

    except Exception as e:
        print(e)
        print("No results. Try a new Search.")


# TODO Satvik
def search_album(album):
    try:
        CURSOR.execute("SELECT * FROM p320_19.albums WHERE name=%s",
                       album)

        rows = CURSOR.fetchall()

        for row in rows:
            print("Album: ", row[2], "Release Date: ", row[1])
            CURSOR.execute("SELECT * FROM p320_19.artists WHERE "
                           "artistid=%s", (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Artist: ", r[1])

            CURSOR.execute("SELECT * FROM p320_19.genre WHERE genreid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Genre: ", r[1])

            CURSOR.execute("SELECT * FROM p320_19.songs WHERE songid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Song: ", row[2], "Release Date: ", row[1],
                      "Duration: ", row[3])

    except Exception as e:
        print(e)
        print("No results. Try a new Search.")


# TODO Satvik
def search_genre(genre):
    try:
        CURSOR.execute("SELECT * FROM p320_19.genre WHERE name=%s",genre)

        rows = CURSOR.fetchall()

        for row in rows:
            print("Genre: ", row[1])
            CURSOR.execute("SELECT * FROM p320_19.albums WHERE albumid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Album: ", r[2], "Release Date: ", r[1])

            CURSOR.execute("SELECT * FROM p320_19.artists WHERE artistid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Artist: ", r[1])

            CURSOR.execute("SELECT * FROM p320_19.songs WHERE songid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Song: ", row[2], "Release Date: ", row[1],
                      "Duration: ", row[3])

    except Exception as e:
        print(e)
        print("No results. Try a new Search.")


# TODO Satvik
def search_artist(artist):
    try:
        CURSOR.execute("SELECT * FROM p320_19.artists WHERE name=%s",
                       artist)

        rows = CURSOR.fetchall()

        for row in rows:
            print("Artist: ", row[1])
            CURSOR.execute("SELECT * FROM p320_19.albums WHERE albumid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Album: ", r[2], "Release Date: ", r[1])

            CURSOR.execute("SELECT * FROM p320_19.genre WHERE genreid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Genre: ", r[1])

            CURSOR.execute("SELECT * FROM p320_19.songs WHERE songid=%s",
                           (row[0]))
            rows1 = CURSOR.fetchall()
            for r in rows1:
                print("Song: ", row[2], "Release Date: ", row[1],
                      "Duration: ", row[3])

    except Exception as e:
        print(e)
        print("No results. Try a new Search.")


# TODO
def follow(email):
    ids = ['abc', 'xyz', 'mno']
    if email in ids:
        print("You now follow " + email)
    else:
        print("Wrong email. Please enter correct email!")


# TODO
def unfollow(email):
    # need to check if user follows the username
    ids = ['abc', 'xyz', 'mno']
    if email in ids:
        print("You unfollowed " + email)
    else:
        print("Wrong email. Please enter correct email!")


# finished Justin
def create_playlist(name):
    try:
        CURSOR.execute(create_playlist_SQL, (name, USERNAME))
        print(f"playlist {name} created")
    except Exception as e:
        print("error creating playlist")
    finally:
        CONNECTION.commit()


# finished Ishan
def delete_playlist(playlist):
    # check if playlist has songid
    if user_playlist_check(playlist):
        try:
            CURSOR.execute(delete_playlist_sql, (playlist,))
            CURSOR.execute(delete_song_with_playlist, (playlist,))
            CURSOR.execute(delete_album_with_playlist, (playlist,))
            CONNECTION.commit()
            print(f"Playlist id:{playlist} deleted")

        except Exception as e:
            print(e)
        finally:
            CONNECTION.commit()
    else:
        print(f"You do not own a playlist with id:{playlist}")


# finished Justin
def add_playlist_song(playlist, songid):
    if user_playlist_check(playlist):
        try:
            CURSOR.execute(add_song_playlist_SQL, (playlist, songid))
            CONNECTION.commit()
            print(f"song id:{songid} added to playlist id:{playlist}")
        except:
            print(f"song id:{songid} already in playlist id:{playlist}")
        finally:
            CONNECTION.commit()
    else:
        print(f"You do not own a playlist with id:{playlist}")


# finished Ishan
def delete_playlist_song(playlist, songid):
    # check if playlist has songid
    if user_playlist_check(playlist):
        try:
            CURSOR.execute(select_songs_in_playlist, (playlist,))
            if CURSOR.fetchone() is None:
                print(
                    f"song id:{songid} doesnot exist in playlist id:{playlist}")
            else:
                CURSOR.execute(delete_playlist_song_sql,
                               (playlist, songid))
                CONNECTION.commit()
                print(
                    f"song id:{songid} deleted from playlist id:{playlist}")
        except Exception as e:
            print(e)
        finally:
            CONNECTION.commit()
    else:
        print(f"You do not own a playlist with id:{playlist}")


# finished Ishan
def add_playlist_album(playlist, albumid):
    if user_playlist_check(playlist):
        try:
            CURSOR.execute(add_album_playlist_SQL, (playlist, albumid))
            CONNECTION.commit()
            print(f"album id:{albumid} added to playlist id:{playlist}")
        except:
            print(f"album id:{albumid} already in playlist id:{playlist}")
        finally:
            CONNECTION.commit()
    else:
        print(f"You do not own a playlist with id:{playlist}")


# finished Ishan
def delete_playlist_album(playlist, albumid):
    # check if playlist has songid
    if user_playlist_check(playlist):
        try:
            CURSOR.execute(select_albums_in_playlist, (playlist,))
            if CURSOR.fetchone() is None:
                print(
                    f"album id:{albumid} doesnot exist in playlist id:{playlist}")
            else:
                CURSOR.execute(delete_playlist_album_sql,
                               (playlist, albumid))
                CONNECTION.commit()
                print(
                    f"album id:{albumid} deleted from playlist id:{playlist}")
        except Exception as e:
            print(e)
        finally:
            CONNECTION.commit()
    else:
        print(f"You do not own a playlist with id:{playlist}")


# finished Justin
def change_playlist_name(playlistid, newname):
    if user_playlist_check(playlistid):
        try:
            CURSOR.execute(change_playlist_name_SQL, (newname, playlistid))
            print(f"Changed playlist id:{playlistid} name to {newname}")
        except Exception as e:
            print(e)
        finally:
            CONNECTION.commit()
    else:
        print(f"You do not own a playlist with id:{playlistid}")


# finished Ishan
def show_friends():
    try:
        CURSOR.execute(show_friends_sql, (USERNAME,))

        if CURSOR.fetchone() is None:
            print("You have no friends")

        else:
            # print friends
            print("Your playlists are: ")
            for p in CURSOR.fetchall():
                # Use str.join() to convert tuple to string.
                data = ''.join(p)
                print(data)
    except Exception as e:
        print(e)


# finished Ishan
# Collection’s name
# – Number of songs in the collection : finished by Justin
# – Total duration in minutes : finished by Justin
def show_playlists():
    try:
        CURSOR.execute(show_playlists_sql, (USERNAME,))

        if CURSOR.fetchone() is None:
            print("You have no playlists")

        else:
            # print playlists
            print("Your playlists are: ")
            for p in CURSOR.fetchall():

                # this grabs number of songs
                CURSOR.execute(
                    f"SELECT count(*) from p320_19.collection_songs WHERE playlistid={p[0]};")
                num_songs = CURSOR.fetchone()[0]
                CURSOR.execute(
                    f"SELECT count(*) from p320_19.collection_albums INNER JOIN p320_19.collected_songs a on collection_albums.\"albumID\" = a.albumid WHERE playlistid={p[0]};")
                num_songs += CURSOR.fetchone()[0]

                # this grabs total duration
                CURSOR.execute(
                    f"SELECT sum(s.duration) from p320_19.collection_songs INNER JOIN p320_19.songs s on collection_songs.songid = s.songid WHERE playlistid={p[0]};")
                # duration = str(CURSOR.fetchone()[0]).split(":")
                # print(CURSOR.fetchone()[0])
                time = str(CURSOR.fetchone()[0]).split(":")
                duration = None
                if time[0] != 'None':
                    hours = int(time[0])
                    minutes = int(time[1])
                    seconds = float(time[2])
                    duration = datetime.timedelta(hours=hours,
                                                  minutes=minutes,
                                                  seconds=seconds)
                # duration = CURSOR.fetchone()[0]
                CURSOR.execute(
                    f"SELECT sum(s.duration) from p320_19.collection_albums ca INNER JOIN p320_19.albums a on ca.\"albumID\" = a.albumid INNER JOIN p320_19.collected_songs c on a.albumid = c.albumid INNER JOIN p320_19.songs s ON s.songid = c.songid WHERE playlistid={p[0]};")
                time = str(CURSOR.fetchone()[0]).split(":")
                if time[0] != 'None':
                    hours = int(time[0])
                    minutes = int(time[1])
                    seconds = float(time[2])
                    if duration is None:
                        duration = datetime.timedelta(hours=hours,
                                                      minutes=minutes,
                                                      seconds=seconds)
                    else:
                        duration += datetime.timedelta(hours=hours,
                                                       minutes=minutes,
                                                       seconds=seconds)

                # Use str.join() to convert tuple to string.
                # data = ''.join(p)
                # print (data)
                print(
                    f"id:{str(p[0])}, Name:{p[1]}, number of songs:{num_songs}, duration {duration}")
    except IndexError as e:
        print(e)


# TODO
def search_user(string):
    user = ["xyz", "mno", "is4761", "ishan"]
    for u in user:
        if u[:len(string)] == string:
            print("Found " + u)


# "finished" Justin
# works for now but user can't play same song twice on same day because databse uses date as primary key.
# will fix when database is updated
def play_song(songid):
    CURSOR.execute(f"SELECT name from p320_19.songs WHERE songid={songid}")
    song_name = CURSOR.fetchone()
    if song_name is None:
        print(f"song id:{songid} does not exist")
        return
    try:
        current_date = str(datetime.datetime.now())
        CURSOR.execute(play_song_SQL, (songid, USERNAME, current_date))
        print(f"playing {song_name[0]}........")
    except Exception as e:
        print(e)
    finally:
        CONNECTION.commit()


# TODO Justin
def play_playlist(playlistid):
    CURSOR.execute(
        f"SELECT name from p320_19.playlists WHERE playlistid={playlistid}")
    playlist_name = CURSOR.fetchone()
    if playlist_name is None:
        print(f"playlist id:{playlistid} does not exist")
        return
    CURSOR.execute(select_songs_in_playlist, (playlistid,))
    song_ids = CURSOR.fetchall()
    CURSOR.execute(select_albums_in_playlist, (playlistid,))
    album_ids = CURSOR.fetchall()
    if not song_ids and not album_ids:
        print(f"playlist {playlist_name[0]} has no songs or albums")
        return
    for song in song_ids:
        play_song(song[0])
    for album in album_ids:
        CURSOR.execute(
            f"SELECT songid from p320_19.collected_songs WHERE albumid={album[0]};")
        songs = CURSOR.fetchall()
        for song in songs:
            play_song(song[0])


def init():
    global CONNECTION, CURSOR
    CONNECTION = sqlconnect.connect()
    CURSOR = CONNECTION.cursor()


# check if playlist belongs to user or not
def user_playlist_check(playlistid):
    try:
        CURSOR.execute(user_playlistid_check_sql, (USERNAME,))
        results = CURSOR.fetchall()
        for id in results:
            if str(id[0]) == str(playlistid):
                return True
        return False
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    login()






