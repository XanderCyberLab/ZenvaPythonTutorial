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

def list_tasks(selected_user):
    for tasks in users_task:
        print(tasks)

def new_user():
    username = input(new_user_prompt)
    users_database.append(username)
    print("New User Created: " + username + "\n")
    
def new_task(selected_user):
    print(f"Please enter a new task for {selected_user}:\n")
    task_name = input()
    task = f"{selected_user}: {task_name}"
    users_task.append(task)
    print(f"New task '{task}' created for {selected_user}\n")    

def task_user(selected_user):#Passes the selected user from select_user function
    task_selection = input(tasks_prompt)
    if task_selection == "1":
        list_tasks(selected_user)
    elif task_selection == "2":
        new_task(selected_user)#Passes the selected user to new_task function
    else:
        return ""
    
def select_user():
    print("Select a User\n")
    for index, username in enumerate(users_database):#For loop with enumerate is to # the list
        print(f'{index + 1}. {username}')
    user_selection = int(input()) - 1 #-1 is to make the list start at 0
    selected_user = users_database[user_selection] #This is to select the user from the list  
    print(f'Welcome {selected_user}\n')
    return selected_user #This is to return the selected user to the main function

def main():
    while True:
        selection = input(welcome_prompt)
        if selection == "1":
            list_users()
        elif selection == "2":
            new_user()
        elif selection == "3":
            selected_user = select_user()#Creates a variable and returns the selected user from select user function
            task_user(selected_user)#With selected user variable, it is passed to task_user function
        else:
            return ""
            
main()
                
