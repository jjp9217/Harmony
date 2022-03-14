"""
@author: Ishan Shah
file name: main.py
"""

from turtle import clearscreen


LOGIN = False

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
    print("--follow 'email'")
    print("--unfollow 'email'")
    print("--create playlist 'name'")
    print("--playlist 'name' add 'songid")
    print("--search name 'song name'")
    print("--search artist 'song artist'")
    print("--search album 'song album'")
    print("--search genre 'song genre'")
    print("--logout")


def follow(email):
    ids = ['abc','xyz','mno']
    if username in users:
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

def add_playlist(name,songid):
    # check if playlist has songid
    if(1):
        print("Song " +songid+  " added to "+ name)
    else:
        print("Song already exists")

def main():
    print("-----Welcome to Harmony-----")
    print("Do you want to login or register?")
    signup = input("Enter login to login and register to create a new account with Harmony: ")
    if(signup =="register"):
        print("You have registered!")
    while not LOGIN:
        login()
    help()
    while(LOGIN):
        command = input("\nEnter command: ")
        if(command == "help" ):
            help()
        elif(command == "logout"):
            logout()
        elif(command[:6] == "follow"):
            follow(command[7:])
        elif(command[:8] == "unfollow"):
            unfollow(command[9:])
        elif(command[:10]=="create playlist"):
            create_playlist(command[11:])
        # need to edit to add albums
        elif(command.split(" ")[0]=="playlist" and command.split(" ")[2]=="add"):
            add_playlist(command.split(" ")[1],command.split(" ")[3])
        elif(command[:6]==search):
            if(command[6:12]=="artist"):
                search_artist(command[12:])
            elif(command[6:11]=="album"):
                search_album(command[10:])
            elif(command[6:10]=="name"):
                search_name(command[10:])
            elif(command[6:11]=="genre"):
                search_genre(command[11:])
        else:
            print("Invalid command. Try 'help' to get help!")
    exit()

main()