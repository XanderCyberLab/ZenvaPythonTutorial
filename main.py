print("Medical Diagnose Bot")
welcome_prompt = "Welcome Doctor! Please choose an option from the menu below\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "What is the patient's name?\n"
apperance_prompt = "How's the patient general appearance?\n - 1: Normal apperance\n - 2: Irritable or lethargic\n"

def list_patients():
    print("Listing patients")

def run_diagnosis():
    name = input(name_prompt)
    apperance = input(apperance_prompt)

def main():     
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            run_diagnosis()
        elif selection == "q":
            return

main()
