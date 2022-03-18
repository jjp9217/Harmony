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

create_playlist_SQL = "INSERT INTO p320_19.playlists(playlistid, name, username) Values (%s,%s, %s);"

# TODO
search_user_SQL = "SELECT * FROM p320_19.dummy;"

user_login_check_sql = "select * from p320_19.\"user\" where username = '%s' and password = '%s';"

global CONNECTION

"""
    User action functions
"""
def register():

        # First, open a database connection
        connection = sqlconnect.connect()

        # Create a cursor. It allows us to execute SQL commands.
        cursor = connection.cursor()

        ### Build the user input

        username = input("Provide a new username: >")

        #Make sure the username is unique -- it is the key for the "users" table
        unique = False
        while not unique:

                cursor.execute(user_exists_sql, username)
                entries = cursor.fetchall()
                if len(entries) > 0:
                        print("The username '" + username +"' is taken")
                        username = input("provide a new username: >")
                        continue
                else:
                        unique = True


        password = input("Provide a new password: >")
        email = input("Provide an email address: >")
        f_name = input("First name: >")
        l_name = input("Last name: >")
        current_date = str(datetime.date.today()) #cast date to yyyy-mm-dd string


        # Now try to add this person to the DB.
        cursor.execute(register_sql, (username, current_date, password,  f_name, l_name, email ))

        # Make the change
        connection.commit()

        # Terminate connection
        sqlconnect.disconnect(connection)


# TODO
def login():
    global LOGIN
    username = input("Enter username: ")
    password = input("Enter password: ")
    if(username == "ishanshah" and password =="123"):
        LOGIN = True
    else:
        print("Username or password is wrong. Try again!")


# TODO this just need to exit main
def logout():
    sqlconnect.disconnect(conn)


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
    # cannot create playlist with same name
    # playlist_name=["sleep","gym"]
    # if name not in playlist_name:
    #     playlist_name+=[name]
    # else:
    try:

    except:
        print("Playlist name already exists. Choose new name!")


# TODO Justin
def add_playlist_song(name, songid):
    # check if playlist has songid
    if(1):
        print("Song " +songid+  " added to "+ name)
    else:
        print("Song already exists")


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


# TODO
def show_friends():
    print("You have x friends. They are: ")


# TODO
def show_playlists():
    print("You have x playlists. They are: ")


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
    conn = sqlconnect.connect()
    curs = conn.cursor()


if __name__ == "__main__":
        register()


