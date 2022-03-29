"""
@author: Ishan Shah
@author: Jesse Pingitore
file name: main.py
Dependencies: psycopg2, sshtunnel
"""
from harmonySQL import *

def help():
    print("Commands to run:")
    print("--help")
    print("--play song 'songid'")
    print("--play playlist 'playlistid'") #playing albums not part of reqs
    print("--follow 'username'")
    print("--unfollow 'username'")
    print("--create playlist 'name'")#does not work if ' or " in the name
    print("--playlist 'id' add song 'songid'")
    print("--playlist 'id' add album 'albumid'")
    print("--playlist 'id' delete song 'songid'")
    print("--playlist 'id' delete album 'albumid'")
    print("--playlist 'id' change-name 'new name'")
    print("--search user 'email'")
    print("--search songname 'song name'")
    print("--search artist 'song artist'")
    print("--search album 'song album'")
    print("--search genre 'song genre'")
    print("--sort 'songname/genre/artist/album' 'asc/desc'")
    print("--delete playlist 'id'")
    print("--top songs")
    print("--top friend songs")
    print("--top genres")
    print("--show friends")
    print("--show playlists")
    print("--logout")

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

        if command == "showme":#TODO put in user profile stuf here
            pass

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

        elif command == "top songs":
            pass

        elif command == "top friend songs":
            pass

        elif command == "top genres":
            pass

        else:
            print(error_message)


if __name__ == "__main__":
    main()


