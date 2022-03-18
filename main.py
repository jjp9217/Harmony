"""
@author: Ishan Shah
@author: Jesse Pingitore
file name: main.py
Dependencies: psycopg2, sshtunnel
"""
import sqlconnect
from harmonySQL import *

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

def main():
    conn = sqlconnect.connect()
    curs = conn.cursor()

    print("-----Welcome to Harmony-----")
    print("Do you want to login or register?")
    signup = input("Enter login to login and register to create a new account with Harmony: ")
    if(signup =="register"):
        register()

    #implicitly accept all other input as "Login"
    #TODO we should handle a user creating an account also as a login
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


if __name__ == "__main__":
    main()


