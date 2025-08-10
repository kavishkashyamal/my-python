import datetime
import json
import guest

file_path = r"user_list.json"
date = datetime.datetime.now()
print(f"Today is {date.strftime('%Y')} {date.strftime('%b')} {date.strftime('%d')}. Welcome to NoCode.com...")

print("Please log-in to continue...")

'''Open the file'''
with open(file_path,'r') as list:
    userlist = json.load(list)


def login():
    status = False
    uname = input("Enter Your username here : ")
    pword = input("Enter your password here : ")
    while True:
        for user in userlist:
            if uname == user['username'] and pword == user['password']:
                print("Welcome to NoCode.com")


def user_or_guest():
    user_or_guest = input("User(1) or Guest(2) : ")
    if user_or_guest == '1':
        login()
    else:
        guest.guest()

user_or_guest()

