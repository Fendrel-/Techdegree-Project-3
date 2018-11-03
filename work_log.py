import os
import csv

import classes

# Clears the console screen when function is called between menu changes.
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Run the 'find  by date' function if user selects it from the main menu.
def find_by_date():
    header('Find by Date')
    input(' This is a placeholder for a function. (Press enter)')

# Run the 'find by time spent' function if user selects it from the search menu.
def find_by_time():
    header('Find by Time')
    input(' This is a placeholder for a function. (Press enter)')

# Run the 'find by exact match' function if user selects it from the search menu.
def find_by_exact():
    header('Find by Exact Name')
    input(' This is a placeholder for a function. (Press enter)')

# Run the 'find by pattern' function if user selects it from the search menu.
def find_by_pattern():
    header('Find by Pattern')
    input(' This is a placeholder for a function. (Press enter)')

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
        col1_width = 13
        col2_width = 25
        col3_width = 10
        header('All Entries')
        print('\n Date Added' + ' ' * (col1_width - 10), end="")
        print('Task' + ' ' * (col2_width - 4), end="")
        print('Minutes' + ' ' * (col3_width - 7), end="")
        print('Notes', end="")
        print('\n ', end="")
        print('-' * 70)
        with open('tasks.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                print(' ' + row[0] + ' ' * (col1_width - len(row[0])), end="")
                print(row[1] + ' ' * (col2_width - len(row[1])), end="")
                print(row[2] + ' ' * (col3_width - len(row[2])), end="")
                print(row[3])

        classes.Menu(
            status_message)
        menu_choice = menu_prompt()
        if menu_choice == "1":
            clear()
            break
        elif menu_choice == "2":
            clear()
            quit()

# Run the 'add entry' function if user selects it from the main menu.
def add_entry():
    header('Add a Task')
    task_name = input('\n What is the task name? ')
    while len(task_name) > 20:
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
    task = classes.Task(task_name, time_spent, notes)
    task.write_to_file()
    clear()
    return "New Entry Added Successfully!"

# Run the search menu if user selects it from the main menu.
def search_menu():
    status_message = None
    while True:
        header('Search Entries')
        classes.Menu(
            status_message,
            "Find By Date",
            "Find By Time Spent",
            "Find By Exact Name",
            "Find By Pattern",)
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
            clear()
            break
        elif menu_choice == "6":
            clear()
            quit()

# Display the top-level menu on program start.
def top_menu(status_message):
    while True:
        header('Work Log')
        classes.MainMenu(
            status_message,
            'Add New Entry',
            'Show All Entries',
            'Search Entries')
        menu_choice = menu_prompt()
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
