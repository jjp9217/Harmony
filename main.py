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
    print("--follow 'username'")
    print("--logout")


def follow(username):
    users = ['abc','xyz','mno']
    if username in users:
        print("You now follow "+username)
    else:
        print("Wrong username. Please enter correct username!")


def main():
    print("Welcome to Harmony")
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
        else:
            print("Invalid command. Try 'help' to get help!")
    exit()

# if '__name__'=='__main__':
#     main()
main()