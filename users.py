import modulefile as mf


def authorize():
    usr = mf.get_users()
    if usr == False: return False

    while True:
        username: str = input("Enter username or :c to create a new user or :q to exit app\n")

        if username == ":q":
            return False

        if username == ":c":
            username = create_user(usr)
            return username

        if username in usr:
            return username

        print("There is no user named ", username, ". Type :c if you want to create a new one.")


def create_user(usr: set):
    while True:
        new_usr = input("Enter your name\n")

        if new_usr == ":q": return False

        if not new_usr in usr:
            mf.add_usr(new_usr)
            return new_usr
        print("There is a user with name ", new_usr, ". Please, try again")