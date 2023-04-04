options = ['option1', 'option2', 'option3']
print('Please select an option:')
for index, option in enumerate(options):
    print(f'{index + 1}. {option}')

selected_option = int(input()) - 1
print(f'You selected: {options[selected_option]}')


def select_user():
    print("Select a User\n")
    for index, username in enumerate(users_database):
        print(f'{index + 1}. {users_database}')
    user_selection = int(input() - 1)
    
    print("Welcome " + user_selection + "\n")
    task_user()