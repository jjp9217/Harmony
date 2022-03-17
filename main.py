"""
@author: Ishan Shah
@author: Jesse Pingitore
file name: main.py
Dependencies: psycopg2, sshtunnel
"""
import sqlconnect

LOGIN = False


def register():
    print("You have registered!")

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

def help():
    print("\n")
    print("Commands to run:")
    print("--help")
    print("--play song 'songid")
    print("--play album 'albumid'")
    print("--play playlist 'playlistname'")
    print("--follow 'email'")
    print("--unfollow 'email'")
    print("--create playlist 'name'")
    print("--playlist 'name' add song 'songid")
    print("--playlist 'name' add album 'albumid")
    print("--playlist 'name' delete song 'songid")
    print("--playlist 'name' delete album 'albumid")
    print("--playlist 'name' change name 'new name")
    print("--search user 'string'")
    print("--search songname 'song name'")
    print("--search artist 'song artist'")
    print("--search album 'song album'")
    print("--search genre 'song genre'")
    print("--show friends")
    print("--show playlists")
    print("--logout")


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


def main():
    conn = sqlconnect.connect()
    curs = conn.cursor()

    print("-----Welcome to Harmony-----")
    print("Do you want to login or register?")
    signup = input("Enter login to login and register to create a new account with Harmony: ")
    if(signup =="register"):
        register()
    while not LOGIN:
        login()
    help()
    while(LOGIN):
        command = input("\nEnter command: ")
        split = command.split(" ")
        if(command == "help" ):
            help()
        elif(command == "logout"):
            logout()
        elif(split[0] == "follow"):
            follow(split[1])
        elif(split[0] == "unfollow"):
            unfollow(split[1])
        elif(split[0]=="create playlist"):
            create_playlist(split[1])
        elif(split[0]=="playlist" and split[2]=="add" and split[3]=="song"):
            add_playlist_song(split[1],split[4])
        elif(split[0]=="playlist" and split[2]=="delete" and split[3]=="song"):
            delete_playlist_song(split[1],split[4])
        elif(split[0]=="playlist" and split[2]=="add" and split[3]=="album"):
            add_playlist_album(split[1],split[4])
        elif(split[0]=="playlist" and split[2]=="delete" and split[3]=="album"):
            delete_playlist_album(split[1],split[4])
        elif(split[0]=="search"):
            #search with sorted value
            if(split[1]=="artist"):
                search_artist(split[2])
            elif(split[1]=="album"):
                search_album(split[2])
            elif(split[1]=="songname"):
                search_name(split[2])
            elif(split[1]=="genre"):
                search_genre(split[2])
            elif(split[1]=="user"):
                search_user(split[2])
        elif(split[0]=="playlist" and split[2]=="change" and split[3]=="name"):
            change_playlist_name(split[1],split[4])
        elif(split[0]=="show"):
            if(split[1]=="friends"):
                show_friends()
            elif(split[1]=="playlists"):
                show_playlists()
        else:
            print("Invalid command. Try 'help' to get help!")
    sqlconnect.disconnect(conn)
    exit()

main()