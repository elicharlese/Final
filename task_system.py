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

opt = None

while True:
    print_main_menu(the_menu) # TODO 2: define the function, uncomment, and call with the menu as an argument
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters
    if opt not in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue
    print(f"You selected option {opt} to > {the_menu[opt]}.")
    if opt == 'q': # TODO 4: quit the program
        print("Goodbye!\n")
        break # exit the main `while` loop
    # Pause before going back to the main menu
    input("::: Press Enter to continue")

print("Have a nice day!")
# Back to top