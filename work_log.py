import os

import classes

# Clears the console screen when it is run between menu changes.
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Run the 'find  by date' function if it selected from the main menu.
def find_by_date():
    header('Find by Date')

# Run the 'find by time spent' function if it is selected from the search menu.
def find_by_time():
    header('Find by Time')

# Run the 'find by exact match' function if it is selected from the search menu.
def find_by_exact():
    header('Find by Exact Name')

# Run the 'find by pattern' function if it is selected from the search menu.
def find_by_pattern():
    header('Find by Pattern')
    input(' This is a placeholder for a function. (Press enter)')

# Display the heading with the title of the menu before the
# menu options are displayed.
def header(heading):
    clear()
    print('-' * 35)
    print(' ' + heading)
    print('-' * 35)

# Prompt the user for a menu option.
def menu_prompt():
    return input('\n Choose an option: ')

# Run the 'display entries' function if it is run from the main menu.
def display_entries():
    status_message = None
    while True:
        header('All Entries')
        classes.Menu(
            status_message)
        menu_choice = menu_prompt()
        if menu_choice == "1":
            clear()
            break
        elif menu_choice == "2":
            clear()
            quit()

# Run the 'add entry' function if it is selected from the main menu.
def add_entry():
    header('Add a Task')
    task_name = input('\n What is the task name? ')
    time_spent = input(' How many minutes were spent on this task? ')
    print('-----------(Optional)-----------')
    notes = input('Enter any notes. ')
    task = classes.Task(task_name, time_spent, notes)
    task.write_to_file()
    clear()
    return "New Entry Added Successfully!"

# Run the search menu if it is selected from the main menu.
def search_menu():
    status_message = None
    while True:
        header('Search Entries')
        classes.Menu(
            status_message,
            "Find By Date",
            "Find By Time Spent",
            "Find By Exact Name",
            "Find By Pattern",
            "Find By Telekinesis")
        menu_choice = menu_prompt()
        if menu_choice == "1":
            find_by_date()
        if menu_choice == "2":
            find_by_time()
        if menu_choice == "3":
            find_by_exact()
        if menu_choice == "4":
            find_by_pattern()
        if menu_choice == "5":
            status_message = 'Nah, I\'m just kidding, \
don\'t\n bend the spoon, that\'s impossible!\
\n\n Achievement unlocked\n 250G - Neo != The One'
        if menu_choice == "6":
            clear()
            break
        elif menu_choice == "7":
            clear()
            quit()

# Display the top-level menu on program start.
def top_menu():
    status_message = None
    while True:
        header('Main Menu')
        classes.MainMenu(
            status_message,
            'Add New Entry',
            'Show All Entries',
            'Search Entries')
        menu_choice = menu_prompt()
        if menu_choice == "1":
            status_message = add_entry()
        if menu_choice == "2":
            status_message = display_entries()
        elif menu_choice == "3":
            status_message = search_menu()
        elif menu_choice == "4":
            clear()
            quit()
        else:
            menu = classes.Menu(
                'Main Menu',
                'I\'m sorry, that\'s not a valid option.',
                'Add New Entry',
                'Search Entries')

# Allow the program to run if the script is run directly.
if __name__ == "__main__":
    while True:
        top_menu()
