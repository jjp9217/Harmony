"""
@author Jesse Pingitore
file: harmonySQL.py
This file acts as a utility dump for the SQL calls.
It holds both the string templates for the calls, and functions for different user actions.
"""
import datetime

import sqlconnect

"""
    Constants
"""
register_sql = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
      "values (%s, %s, %s, %s, %s, %s);"

user_exists_sql = "select * from p320_19.\"user\" where username = '%s'"



def register():

        # First, open a database connection
        connection = sqlconnect.connect()

        # Create a cursor. It allows us to execute SQL commands.
        cursor = connection.cursor()

        ### Build the user input

        username = input("provide a new username: >")

        #TODO Select the DB to find if this username is taken

        password = input("provide a new password: >")
        email = input("provide an email address: >")
        f_name = input("first name: >")
        l_name = input("last name: >")
        current_date = str(datetime.date.today()) #cast date to yyyy-mm-dd string


        # Now try to add this person to the DB.
        cursor.execute(register_sql, (username, current_date, password,  f_name, l_name, email ))

        # Make the change
        connection.commit()

        # Terminate connection
        sqlconnect.disconnect(connection)



def login():
    global LOGIN
    username = input("Enter username: ")
    password = input("Enter password: ")
    if(username == "ishanshah" and password =="123"):
        LOGIN = True
    else:
        print("Username or password is wrong. Try again!")
    
def logout():
    global LOGIN
    LOGIN = False


def search_name(songname):
    print(songname)

def search_album(album):
    print(album)

def search_genre(genre):
    print(genre)

def search_artist(artist):
    print(artist)

def follow(email):
    ids = ['abc','xyz','mno']
    if email in ids:
        print("You now follow "+email)
    else:
        print("Wrong email. Please enter correct email!")

def unfollow(email):
    # need to check if user follows the username
    ids = ['abc','xyz','mno']
    if email in ids:
        print("You unfollowed "+email)
    else:
        print("Wrong email. Please enter correct email!")


def create_playlist(name):
    # cannot create playlist with same name
    playlist_name=["sleep","gym"]
    if name not in playlist_name:
        playlist_name+=[name]
    else:
        print("Playlist name already exists. Choose new name!")

def add_playlist_song(name,songid):
    # check if playlist has songid
    if(1):
        print("Song " +songid+  " added to "+ name)
    else:
        print("Song already exists")


def delete_playlist_song(name,songid):
    # check if playlist has songid
    if(1):
        print("Song " +songid+  " added to "+ name)
    else:
        print("Song doesnot exist")


def add_playlist_album(name,albumid):
    # check if playlist has albumid
    if(1):
        print("Album " +albumid+  " added to "+ name)
    else:
        print("Album already exists")


def delete_playlist_album(name,albumid):
    # check if playlist has albumid
    if(1):
        print("Album " +albumid+  " added to "+ name)
    else:
        print("Album doesnot exist")

def change_playlist_name(ogname,newname):
    print("Changed from "+ ogname+ " to " + newname)

def show_friends():
    print("You have x friends. They are: ")

def show_playlists():
    print("You have x playlists. They are: ")


def search_user(string):
    user=["xyz","mno","is4761","ishan"]
    for u in user:
        if u[:len(string)]==string:
            print("Found " +u)

def play():
        print("Played")


if __name__ == "__main__":
        register()


