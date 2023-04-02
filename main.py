print("Medical Diagnose Bot")
welcome_prompt = "Welcome Doctor! Please choose an option from the menu below\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

def list_patients():
    print("Listing patients")

def run_diagnosis():
    print("New Diagnosis")

def main():     
    
    selection = input(welcome_prompt)
    if selection == "1":
        list_patients()
    elif selection == "2":
        run_diagnosis()
    elif selection == "q":
        return

main()
