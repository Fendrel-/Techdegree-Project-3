import os
import datetime
import re

import classes

# Clears the console screen when function is called between menu changes.
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display_menu(status_message, menu_options, is_main_menu):
    if is_main_menu:
        classes.MainMenu(status_message, menu_options)
    else:
        classes.Menu(status_message, menu_options)
    return menu_prompt()

# Run the 'find  by date' function if user selects it from the main menu.
def find_by_date():
    fmt = '%m/%d/%Y'
    header('Find by Date')
    date_search = datetime.datetime.strptime(input('\n Enter a date with format MM/DD/YYYY '), '%m/%d/%Y')
    status_message = None
    classes.DisplayEntries('tasks.csv').FindByDate(date_search)
    menu_options = ['Return to Search']
    menu_choice = display_menu(status_message, menu_options, False)
    if menu_choice == 1:
        search_menu()
    elif menu_choice == 2:
        top_menu()
    elif menu_choice == 3:
        clear()
        quit()

# Run the 'find by time spent' function if user selects it from the search menu.
def find_by_time():
    header('Find by Time')
    time_search = input('\n Enter a number of minutes to search for ')
    status_message = None
    classes.DisplayEntries('tasks.csv').FindByTime(time_search)
    menu_options = ['Return to Search']
    menu_choice = display_menu(status_message, menu_options, False)
    if menu_choice == 1:
        search_menu()
    elif menu_choice == 2:
        top_menu()
    elif menu_choice == 3:
        clear()
        quit()

# Run the 'find by exact match' function if user selects it from the search menu.
def find_by_exact():
    header('Find by Exact Name')
    input(' This is a placeholder for a function. (Press enter)')

# Run the 'find by pattern' function if user selects it from the search menu.
def find_by_regex_pattern():
    header('Find by Pattern')
    input(' Enter a regex pattern')

# Display the heading with the title of the menu before the
# menu options are displayed to the user.
def header(heading):
    clear()
    print('-' * 35)
    print(' ' + heading)
    print('-' * 35)

# Prompt the user for a menu option.
def menu_prompt():
    return input('\n Choose an option: ')

# Run the 'display entries' function if user selects it from the main menu.
def display_entries():
    status_message = None
    while True:
        header('All Entries')
        has_entries = classes.DisplayEntries('tasks.csv').ShowAll()
        if not has_entries:
            status_message = 'You don\'t have any entries yet!'
        menu_options = []
        menu_choice = display_menu(status_message, menu_options, False)
        if menu_choice == "1":
            clear()
            break
        elif menu_choice == "2":
            clear()
            quit()

# Run the 'add entry' function if user selects it from the main menu.
def add_entry():
    header('Add a Task')
    task_date = datetime.datetime.strptime(input('\n Enter task date as MM/DD/YYYY '), '%m/%d/%Y')
    task_date = task_date.strftime('%m/%d/%Y')
    task_name = input(' What is the task name? ')
    while len(task_name) > 40:
        clear()
        header('Add a Task')
        task_name = input('\n I\'m sorry your task name is too long. Try again. ')
    time_spent = input(' How many minutes were spent on this task? ')
    while int(time_spent) not in range(100):
        clear()
        header('Add a Task')
        time_spent = input(' Minutes spent must be less than 100. Try again. ')
    print('-----------(Optional)-----------')
    notes = input(' Enter any notes. ')
    task = classes.Task(task_date, task_name, time_spent, notes)
    task.write_to_file()
    clear()
    return "New was added successfully!"

# Run the search menu if user selects it from the main menu.
def search_menu():
    status_message = None
    while True:
        header('Search Entries')
        menu_options = ['Find By Date', 'Find By Time Spent', 'Find By Exact Name', 'Find By Regex Pattern']
        menu_choice = display_menu(
            status_message,
            menu_options,
            False)
        if menu_choice == "1":
            find_by_date()
        if menu_choice == "2":
            find_by_time()
        if menu_choice == "3":
            find_by_exact()
        if menu_choice == "4":
            find_by_pattern()
        if menu_choice == "5":
            clear()
            break
        elif menu_choice == "6":
            clear()
            quit()

# Display the top-level menu on program start.
def top_menu(status_message):
    while True:
        header('Work Log')
        menu_options = ['Add New Entry', 'Show All Entries', 'Search Entries']
        menu_choice = display_menu(
            status_message,
            menu_options,
            True)
        if menu_choice == "1":
            status_message = add_entry()
            continue
        elif menu_choice == "2":
            status_message = display_entries()
        elif menu_choice == "3":
            status_message = search_menu()
        elif menu_choice == "4":
            clear()
            quit()
        else:
            status_message = 'I\'m sorry that\'s not a valid option'

# Allow the program to run if the script is run directly.
if __name__ == "__main__":
    while True:
        top_menu('Main Menu')
