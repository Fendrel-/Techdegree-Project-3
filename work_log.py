import os

import classes

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def find_by_pattern():
    clear()
    input('This is a placeholder for a function. (Press enter)')

def header(heading):
    clear()
    print('-' * 35)
    print(' ' + heading)
    print('-' * 35)

def menu_prompt():
    return input('\n Choose an option: ')

def search():
    menu = None
    while True:
        if not menu:
            menu = classes.Menu('Search Tasks', '', "Find By Date", "Find By Time Spent", "Find By Exact Name", "Find By Pattern", "Find By Telekinesis")
        menu_choice = menu.prompt()
        if menu_choice == "4":
            find_by_pattern()
            menu = None
        if menu_choice == "5":
            menu = classes.Menu('Search Tasks', 'Nah, I\'m just kidding, you can\'t\n bend the spoon that\'s impossible!\n\n Achievement unlocked\n 250G - Neo != The One', "Find By Date", "Find By Time Spent", "Find By Exact Name", "Find By Pattern", "Find By Telepathy")
        if menu_choice == "6":
            clear()
        elif menu_choice == "7":
            clear()
            quit()

def add_entry():
    header('Add a Task')
    task_name = input('\n What is the task name? ')
    time_spent = input(' How many minutes were spent on this task? ')
    print('-----------(Optional)-----------')
    notes = input('Enter additional notes, otherwise press enter. ')
    clear()
    return "New Entry Added Successfully!"

def top_menu():
    status_message = None
    while True:
        header('Main Menu')
        classes.MainMenu(status_message, 'Add New Entry', 'Search Entries')
        menu_choice = menu_prompt()
        if menu_choice == "1":
            status_message = add_entry()
        elif menu_choice == "2":
            search()
        elif menu_choice == "3":
            clear()
            quit()
        else:
            menu = classes.Menu('Main Menu', 'I\'m sorry, that\'s not a valid option.', 'Add New Entry', 'Search Entries')


if __name__ == "__main__":
    while True:
        top_menu()
