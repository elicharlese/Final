from task_functions import *

the_menu = {
    "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"
}

all_tasks = [
    {
        "name": "Call XYZ",
        "info": "",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    },
    {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority": 5,
        "duedate": '06/02/2022',
        "done": 'no'
    },
    {
        "name": "Finish checkpoint 2 for CSW8",
        "info": "Implement the new functions",
        "priority": 5,
        "duedate": '06/05/2022',
        "done": 'no'
    }
]

list_menu = {
    "A": "all tasks",
    "C": "completed tasks",
    "I": "incomplete tasks"
}

priority_scale = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}

opt = None

while True:
    print_main_menu(the_menu)
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters
    if opt not in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue
    print(f"You selected option {opt} to > {the_menu[opt]}.")
    if opt == 'q': # TODO 4: quit the program
        print("Goodbye!\n")
        break # exit the main `while` loop
    elif opt == 'L':
        if all_tasks == []:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue
        subopt = get_selection(the_menu[opt], list_menu)
        # if subopt == 'A':
        #     print_tasks(all_tasks, priority_scale)
        # elif subopt == 'C':
        #     print_tasks(all_tasks, priority_scale, completed = 'yes')
        # elif subopt == 'I':
        #     print_tasks(all_tasks, priority_scale, completed = 'no')
        # # Pause before going back to the main menu
    input("::: Press Enter to continue")
    continue

print("Have a nice day!")
# Back to top