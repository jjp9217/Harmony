"""
@author Jesse Pingitore
file: harmonySQL.py
This file acts as a utility dump for the SQL call.
It holds both the string templates for the calls, and functions for different user actions.
Note that the actions here are ONLY for user interactions.
Any developer tools should use a different file.
"""
import datetime
import sqlconnect

"""
    Constants -----------------------------------------------------------------
"""
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

show_friends_sql="select following_username FROM p320_19.following where follower_username = %s";

show_playlists_sql="select name FROM p320_19.playlists where username = %s"

add_song_playlist_SQL="INSERT INTO p320_19.collection_songs(playlistid, songid) Values (%s,%s);"

#check if playlist belongs to user
user_playlistid_check_sql="select playlistid FROM p320_19.playlists where username = %s"

change_playlist_name_SQL = "Update p320_19.playlists SET name=%s WHERE playlistid=%s"

play_song_SQL = "INSERT INTO p320_19.listens(songid, username, datetime) VALUES (%s, %s, %s)"

select_songs_in_playlist = "SELECT songid from p320_19.collection_songs WHERE playlistid=%s;"

select_albums_in_playlist = "SELECT \"albumID\" from p320_19.collection_albums WHERE playlistid=%s;"




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

        #Make sure the username is unique -- it is the key for the "users" table
        while True:

                CURSOR.execute(user_exists_sql, (username,)) #Note that even single arguments must be tuple-wrapped
                entries = CURSOR.fetchall()
                if len(entries) > 0:
                        print("The username '" + username +"' is taken")
                        username = input("Provide a new username: >")
                        continue
                else:
                        break

        password = input("Provide a new password: >")
        f_name = input("First name: >")
        l_name = input("Last name: >")
        current_date = str(datetime.date.today()) #cast date to yyyy-mm-dd string

        email = input("Provide an email address: >")

        # Make sure the email is unique -- which is part of project requirements
        while True:

            CURSOR.execute(email_exists_sql, (email,))  # Note that even single arguments must be tuple-wrapped
            entries = CURSOR.fetchall()
            if len(entries) > 0:
                print("The username '" + email + "' is already in use with an account")
                email = input("Provide a different email: >")
                continue
            else:
                break

        # Now try to add this person to the DB.
        CURSOR.execute(register_sql, (username, current_date, password,  f_name, l_name, email ))

        # Make the change
        CONNECTION.commit()
        global USERNAME
        USERNAME = username

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
            print("////// Welcome to Harmony \\\\\\\\\\")
            break

        else:
            print("Username or Password are misspelled, or do not match")
            username = input("Enter username: >")
            password = input("Enter password: >")
    global USERNAME
    USERNAME = username


# finished Justin
def logout():
    sqlconnect.disconnect(CONNECTION)
    print("logged out\nGOODBYE")


# TODO
def search_name(songname):
    print(songname)


# TODO
def search_album(album):
    print(album)


# TODO
def search_genre(genre):
    print(genre)


# TODO
def search_artist(artist):
    print(artist)


# TODO
def follow(email):
    ids = ['abc','xyz','mno']
    if email in ids:
        print("You now follow "+email)
    else:
        print("Wrong email. Please enter correct email!")


# TODO
def unfollow(email):
    # need to check if user follows the username
    ids = ['abc','xyz','mno']
    if email in ids:
        print("You unfollowed "+email)
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



# TODO
def delete_playlist_song(name,songid):
    # check if playlist has songid
    if(1):
        print("Song " +songid+  " added to "+ name)
    else:
        print("Song doesnot exist")


# TODO
def add_playlist_album(name,albumid):
    # check if playlist has albumid
    if(1):
        print("Album " +albumid+  " added to "+ name)
    else:
        print("Album already exists")


# TODO
def delete_playlist_album(name,albumid):
    # check if playlist has albumid
    if(1):
        print("Album " +albumid+  " added to "+ name)
    else:
        print("Album doesnot exist")


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


# TODO this is broken
def show_friends():
    # First, open a database connection
    connection = sqlconnect.connect()

    # Create a cursor. It allows us to execute SQL commands.
    cursor = connection.cursor()

    # Now try to add this person to the DB.
    cursor.execute(show_friends_sql,(USERNAME,))

    # print friends
    print("Your friends are: ")
    while row is not None:
        print(row)
        row = cursor.fetchone()

    # Make the change
    connection.commit()

    # Terminate connection
    sqlconnect.disconnect(connection)


# TODO this is broken
def show_playlists():

    # First, open a database connection
    connection = sqlconnect.connect()

    # Create a cursor. It allows us to execute SQL commands.
    cursor = connection.cursor()

    # Now try to add this person to the DB.
    cursor.execute(show_playlists_sql,(USERNAME,))

    # print playlists
    print("Your playlists are: ")
    while row is not None:
        print(row)
        row = cursor.fetchone()

    # Make the change
    connection.commit()

    # Terminate connection
    sqlconnect.disconnect(connection)



# TODO
def search_user(string):
    user=["xyz","mno","is4761","ishan"]
    for u in user:
        if u[:len(string)]==string:
            print("Found " +u)


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
        current_date = str(datetime.date.today())
        CURSOR.execute(play_song_SQL, (songid, USERNAME, current_date))
        print(f"playing {song_name[0]}........")
    except Exception as e:
        print(e)
    finally:
        CONNECTION.commit()


# TODO Justin
def play_playlist(playlistid):
    CURSOR.execute(f"SELECT name from p320_19.playlists WHERE playlistid={playlistid}")
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
        CURSOR.execute(f"SELECT songid from p320_19.collected_songs WHERE albumid={album[0]};")
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
        CURSOR.execute(user_playlistid_check_sql,(USERNAME,))
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


