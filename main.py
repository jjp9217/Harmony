"""
@author: Ishan Shah
@author: Jesse Pingitore
file name: main.py
Dependencies: psycopg2, sshtunnel
"""
import sqlconnect
from harmonySQL import *


def help():
    print("Commands to run:")
    print("0) --help")
    print("1) --play song 'songid'")
    print("2) --play playlist 'playlistid'") #playing albums not part of reqs
    print("3) --follow 'username'")
    print("4) --unfollow 'username'")
    print("5) --create playlist 'name'")#does not work if ' or " in the name
    print("6) --playlist 'id' add song 'songid'")
    print("7) --playlist 'id' add album 'albumid'")
    print("8) --playlist 'id' delete song 'songid'")
    print("9) --playlist 'id' delete album 'albumid'")
    print("10) --playlist 'id' change-name 'new name'")
    print("11) --search user 'email'")
    print("12) --search songname 'song name'")
    print("13) --search artist 'song artist'")
    print("14) --search album 'song album'")
    print("15) --search genre 'song genre'")
    print("16) --sort 'songname/genre/artist/album' 'asc/desc'")
    print("17) --delete playlist 'id'")
    print("18) --show friends")
    print("19) --show playlists")
    print("20) --logout")

def main():

    init()
    print("----- Connected to Harmony-----")
    LOGIN = False
    while not LOGIN:
        signup = input("Enter 'login' to login, or 'register' to create a new account: >")
        if signup.lower() == "register":
            register()
            LOGIN = True
        elif signup.lower() == "login":
            login()
            LOGIN = True
        else:
            print("Incorrect command!")

    # Print the usage metssage
    print("Tip of the Day: If you don't know an 'id' for a song, album, or playlist, you can search for them by name! \n")
    help()

    while LOGIN:
        error_message="Invalid command. Try 'help' to get help!"
        command = input("\nEnter command: ")
        split = command.split(" ")

        if command == "help":
            help()

        elif command == "logout":
            logout()
            LOGIN = False

        elif split[0] == "follow":
            follow(split[1])

        elif split[0] == "unfollow":
            unfollow(split[1])

        elif split[0] + " " + split[1] == "create playlist":
            create_playlist(split[2])

        elif split[0] == "playlist":

            if split[2]== "add":
                if  split[3] == "album":
                    add_playlist_album(split[1], split[4])
                elif split[3] == "song":
                    add_playlist_song(split[1], split[4])
                else:
                    print(error_message)

            elif split[2]== "delete":
                if split[3]== "album":
                    delete_playlist_album(split[1],split[4])
                elif split[3] == "song":
                    delete_playlist_song(split[1],split[4])
                else:
                    print(error_message)

            elif split[2] == "change-name":
                change_playlist_name(split[1], split[3])

            else:
                print(error_message)

        elif split[0]== "search":
            #search with sorted value
            if split[1]== "artist":
                search_artist(split[2])
            elif split[1]== "album":
                search_album(split[2])
            elif split[1]== "songname":
                search_name(split[2])
            elif split[1]== "genre":
                search_genre(split[2])
            elif split[1]== "user":
                search_user(split[2])
            else:
                print(error_message)

        elif split[0] == "sort":
            if split[1]=="album":
                if split[2]=="asc" or split[2]=="desc":
                    sort("al.name",split[2])
                else:
                    print(error_message)
            elif split[1]=="artist":
                if split[2]=="asc" or split[2]=="desc":
                    sort("a.artist_name",split[2])
                else:
                    print(error_message)
            elif split[1]=="genre":
                if split[2]=="asc" or split[2]=="desc":
                    sort("g.name",split[2])
                else:
                    print(error_message)
            elif split[1]=="songname":
                if split[2]=="asc" or split[2]=="desc":
                    sort("s.name",split[2])
                else:
                    print(error_message)
            else:
                print(error_message)
        
        elif split[0]== "show":

            if split[1]== "friends":
                show_friends()

            elif split[1]== "playlists":
                show_playlists()
            
            else:
                print(error_message)

        elif split[0] == "play":
            if split[1] == "song":
                play_song(split[2])
            elif split[1] == "playlist":
                play_playlist(split[2])
            else:
                print(error_message)

        elif split[0] == "logout":
            logout()
            LOGIN = False

        elif split[0] == "delete":
            if split[1] == "playlist":
                delete_playlist(split[2]) 
            else:
                print(error_message)

        else:
            print(error_message)


if __name__ == "__main__":
    main()


