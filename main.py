welcome_prompt = "Welcome to Wishymashy's Notepad!\n Please Select an Option:\n - 1 List of Users\n - 2 Create a New User\n - 3 Select User\n"
new_user_prompt = "Please enter a new username:\n"
tasks_prompt ="Please select a task:\n 1 - List Saved Tasks\n 2 - Create a Task\n"

users_database = [
    'Alexander',
    'Miriam',
    'Juvia' 
]

users_task = [
    "Test1: Category: Task 1",
    "Test2: Category: Task 2"
]

def list_users():
    for users in users_database:
        print(users)

def list_tasks():
    for tasks in users_task:
        print(tasks)

def new_user():
    username = input(new_user_prompt)
    users_database.append(username)
    print("New User Created: " + username + "\n")
    
def new_task():
    print("Please enter a new task:\n")
    
def select_user():
    print("Select a User\n")
    for index, username in enumerate(users_database):
        print(f'{index + 1}. {username}')
    user_selection = int(input()) - 1    
    print(f'Welcome {users_database[user_selection]}\n')
    task_user()

def task_user():
    task_selection = input(tasks_prompt)
    if task_selection == "1":
        list_task()
    elif task_selection == "2":
        new_task()
    else:
        return ""

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
            return ""
            
main()
                
