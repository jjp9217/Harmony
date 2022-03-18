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

login_SQL = "select * from p320_19.\"user\" where username = '%s' and password = '%s';"

register_SQL = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
      "values (%s, %s, %s, %s, %s, %s);"

create_playlist_SQL = "INSERT INTO p320_19.playlists(name, username) Values (%s, %s);"

# TODO
search_user_SQL = "SELECT * FROM p320_19.dummy;"

user_login_check_sql = "select * from p320_19.\"user\" where username = %s and password = %s;"

show_friends_sql="select following_username FROM following where follower_username = '%s'";

show_playlists_sql="select name FROM playlist where username = '%s'"

add_song_playlist_SQL=""

global CONNECTION
global CURSOR
global USERNAME
global LOGIN

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
        unique = False
        while not unique:

                CURSOR.execute(user_exists_sql, (username,)) #Note that even single arguments must be tuple-wrapped
                entries = CURSOR.fetchall()
                if len(entries) > 0:
                        print("The username '" + username +"' is taken")
                        username = input("Provide a new username: >")
                        continue
                else:
                        unique = True


        password = input("Provide a new password: >")
        email = input("Provide an email address: >")
        f_name = input("First name: >")
        l_name = input("Last name: >")
        current_date = str(datetime.date.today()) #cast date to yyyy-mm-dd string


        # Now try to add this person to the DB.
        CURSOR.execute(register_sql, (username, current_date, password,  f_name, l_name, email ))

        # Make the change
        CONNECTION.commit()

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


# TODO this just need to exit main
def logout():
    sqlconnect.disconnect(CONNECTION)


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


# TODO Justin
def create_playlist(name):
    try:
        CURSOR.execute(create_playlist_SQL, (name, USERNAME))
    except:
        print("error creating playlist")


# TODO Justin
def add_playlist_song(playlist, songid):
    # if 1:
    #     print("Song " +songid+  " added to "+ name)
    # else:
    #     print("Song already exists")
    try:
        CURSOR.execute(create_playlist_SQL, (playlist, songid))
    except:
        print("error adding song")


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


# TODO Justin
def change_playlist_name(ogname,newname):
    print("Changed from "+ ogname+ " to " + newname)


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


# TODO
def play():
        print("Played")


def init():
    global CONNECTION, CURSOR
    CONNECTION = sqlconnect.connect()
    CURSOR = CONNECTION.cursor()


if __name__ == "__main__":
        register()


