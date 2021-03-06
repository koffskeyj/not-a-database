import csv


def user():
    username = input("Username: ")
    password = input("Password: ")
    full_name = input("Full Name: ")
    favorite_number = input("Favorite Number: ")

    info_packet = ("{},{},{},{}\n".format(username, password, full_name, favorite_number))

    read_file = open("users.csv")
    if username in read_file.read():
        print("Sorry, Username taken.")
        user()
    read_file.close()

    with open("users.csv", "a") as outfile:
        outfile.write(info_packet)


def login():
    give_username = input("Please supply username: ")
    give_password = input("Please supply password: ")

    with open("users.csv") as infile:
        authentication_check = csv.DictReader(infile, fieldnames=["username", "password", "full name", "favorite number"])
        for row in authentication_check:
            print(row)
            if give_username in row["username"] and give_password in row["password"]:
                while True:
                    create_or_log = input("Would you like to create a user or log out?? create/log out: ")
                    if create_or_log == "create":
                        user()
                    if create_or_log == "log out":
                        login()

        else:
            print("Incorrect username or password. Please try again.")
            login()


def start():
    starting_input = input("Do you have a username or password? y/n?: ")
    if starting_input == "y":
        login()
    if starting_input == "n":
        user()
        login()

start()



