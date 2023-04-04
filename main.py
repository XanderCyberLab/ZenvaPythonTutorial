welcome_prompt = "Welcome to Wishymashy's All In One Notepad!\n Please Select an Option.\n - 1 List of Users\n - 2 Create a New User\n"
new_user_prompt = "Please enter a new username:\n"

users_database = [
    "Test"
]

def list_users():
    for users in users_database:
        print(users)

def new_user():
    username = input(new_user_prompt)
    users_database.append(username)
    print("New User Created: " + username + "\n")
    
def select_user():
    print("Select a User\n")
    list_users()
    user_selection = input()
    print("Welcome " + user_selection + "\n")
    

def main():
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_users()
        elif selection == "2":
            new_user()
        elif selection == "3":
            select_user()
        else:
            return
            
main()
                
