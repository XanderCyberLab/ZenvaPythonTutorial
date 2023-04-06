welcome_prompt = "Welcome to Wishymashy's Notepad!\n Please Select an Option:\n - 1 List of Users\n - 2 Create a New User\n - 3 Select User\n - 4 Delete User\n - 5 Exit\n"
new_user_prompt = "Please enter a new username:\n"
tasks_prompt ="Please select a task:\n 1 - List Saved Tasks\n 2 - Create a Task\n 3 - Remove a Task\n"


users_database = {
    'Alexander': [],
    'Miriam': [],
}

users_task = [
]


def list_users():
    for user in users_database:
        print(user)

def list_tasks(selected_user):
    print(f'List of Tasks for {selected_user}:\n')
    tasks = users_database[selected_user]
    for task in tasks:
        print(task)

def new_user():
    username = input(new_user_prompt)
    users_database[username] = []
    print(f'New User Created: {username}\n')
    
def new_task(selected_user):
    print(f"Please enter a new task for {selected_user}:\n")
    task = input()
    tasks = users_database[selected_user]#This is to select the tasks from the selected user
    users_database[selected_user].append(task)#This is to add the task to the selected user
    print(f'New Task Created: {task} for user {selected_user}\n') 

def task_user(selected_user):#Passes the selected user from select_user function
    task_selection = input(tasks_prompt)
    if task_selection == "1":
        list_tasks(selected_user)
    elif task_selection == "2":
        new_task(selected_user)#Passes the selected user to new_task function
    elif task_selection == "3":
        remove_task(selected_user)
    else:
        return ""
    
def select_user():
    print("Select a User\n")
    for index, username in enumerate(users_database):#For loop with enumerate is to # the list
        print(f'{index + 1}. {username}')
    user_selection = int(input()) - 1 #-1 is to make the list start at 0
    selected_user = list(users_database.keys())[user_selection] #This is to select the user from the list  
    print(f'Welcome {selected_user}\n')
    task_user(selected_user)
    return selected_user #This is to return the selected user to the main function

def remove_user():
    print("Select a User to Remove")
    for index, username in enumerate(users_database):#For loop with enumerate is to # the list
        print(f'{index + 1}. {username}')
    user_selection = int(input()) - 1 #-1 is to make the list start at 0
    users_database.pop(list(users_database.keys())[user_selection])#This is to select the user from the list and remove it
    print(f'User {user_selection} removed\n')
    
def remove_task(selected_user):
    print(f'List of Tasks for {selected_user}:\n')
    tasks = users_database[selected_user]
    for index, task in enumerate(tasks):#For loop with enumerate is to # the list
        print(f'{index + 1}. {task}')
    task_selection = int(input()) - 1
    removed_task = tasks.pop(task_selection)#This is to select the task from the list and remove it
    print(f'Task removed: {removed_task}')
    
def main():
    while True:
        selection = input(welcome_prompt)
        if selection == "1":
            list_users()
        elif selection == "2":
            new_user()
        elif selection == "3":
            selected_user = select_user()#Creates a variable and returns the selected user from select user function
            #task_user(selected_user)#With selected user variable, it is passed to task_user function
        elif selection == "4":
            remove_user()
        elif selection == "5":
            exit() 
        else:
            return ""
            
main()
                
