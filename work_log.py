import os

import classes


def add_entry():
    menu = classes.Add('Add New Entry')
    task_name = input(' What is the task name? ')
    time_spent = input(' How many minutes were spent on this task? ')
    print('-----------(Optional)-----------')
    notes = input('Enter additional notes, otherwise press enter. ')

def top_menu():
    menu = classes.Menu('Main Menu', 'Add New Entry', 'Search Entries')
    menu_choice = menu.prompt()
    while True:
        if menu_choice == "1":
            add_entry()
        elif menu_choice == "3":
            os.system('cls')
            quit()
        else:
            menu = classes.Menu('Main Menu', 'Add New Entry', 'Search Entries')
            print("\nI'm sorry, that's not a valid option.\n")
            menu_choice = menu.prompt()


if __name__ == "__main__":
    top_menu()
