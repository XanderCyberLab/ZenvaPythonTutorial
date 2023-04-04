welcome_prompt = "Welcome to Wishymashy's All In One Notepad!\n Please Select an Option.\n - 1 List of Users\n - 2 Create a New User\n"
new_user_prompt = "Please enter a new username:\n"

users_database = [
    "Test"
]

def list_users():
    for username in users_database:
        print(users)

def new_user():
    username = input(new_user_prompt)
    

def main():
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_users()
        elif selection == "2":
            new_user()
        else:
            return
            
main()
                
