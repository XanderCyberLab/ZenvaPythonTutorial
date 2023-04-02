print("Medical Diagnose Bot")
welcome_prompt = "Welcome Doctor! Please choose an option from the menu below\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How's the patient general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eyes_prompt = "Checking Eyes Results:\n - 1 Eyes Normal, Slightly Sunken\n - 2 Eyes Very Sunken\n"
skin_prompt = "Skin Pinch Test Results:\n - 1 Skin is Normal\n - 2 Skin is Slow\n"
normal_appearance = "Check the Eye Appearance\n"
irritable_appearance = "Do a skin pinch\n"
no_dehydration = "No Dehydration"
some_dehydration = "Some Dehydration"
severe_dehydration = "Severe Dehydration"

def list_patients():
    print("Listing patients")

def run_diagnosis():
    name = input(name_prompt)
    appearance = input(appearance_prompt)
    if appearance == "1":
        assess_eyes()
    elif appearance == "2":
        assess_skin()
    else:
        return 

def assess_eyes():
    print(normal_appearance)
    eyes = input(eyes_prompt)
    if eyes == "1":
        print(no_dehydration)
    elif eyes == "2":
        print(severe_dehydration)
    else:
        return


def assess_skin():
    print(irritable_appearance)
    skin = input(skin_prompt)
    if skin == "1":
        print(some_dehydration)
    elif skin == "2":
        print(severe_dehydration)
    else:
        return



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
