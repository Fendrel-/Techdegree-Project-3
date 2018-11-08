import csv
import datetime
import os
import re

import classes


# Display the top-level menu on program start.
def top_menu(status_message):
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
    def modify_entries():
        has_entries = classes.DisplayEntries('tasks.csv').ShowAll()
        def edit_entry(total_entries):
            while True:
                header('Edit an Entry')
                classes.DisplayEntries('tasks.csv').ShowAll()
                entry_number = int(input('\n Select an entry number to edit: ')) - 1
                entry_list = []
                with open('tasks.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        entry_list.append(row)

                clear()
                header('Edit an Entry')
                print('\n [1]   Date:         {} '.format(entry_list[entry_number][0]))
                print(' [2]   Task Name:    {} '.format(entry_list[entry_number][1]))
                print(' [3]   Time Spent:   {} '.format(entry_list[entry_number][2]))
                print(' [4]   Notes:        {} '.format(entry_list[entry_number][3]))
                item_number = int(input('\n Select an item to edit: ')) - 1
                if item_number == 0:
                    try:
                        task_date = datetime.datetime.strptime(input('\n Enter task date as MM/DD/YYYY: '), '%m/%d/%Y')
                        entry_list[entry_number][0] = task_date.strftime('%m/%d/%Y')
                    except ValueError:
                        header('Add a Task')
                        print('\n Please enter a valid date.')
                elif item_number == 1:
                    task_name = input('\n What is the task name?: ')
                    entry_list[entry_number][1] = task_name
                    while len(task_name) > 40:
                        header('Edit an Entry')
                        task_name = input('\n I\'m sorry your task name is too long. Try again: ')
                        entry_list[entry_number][1] = task_name
                elif item_number == 2:
                    try:
                        time_spent = input('\n How many minutes were spent on this task?: ')
                        entry_list[entry_number][2] = int(time_spent)
                        if int(time_spent) > 999:
                            raise ValueError
                    except:
                        return 'Minutes spent must be an integer less that 1,000.'

                elif item_number == 3:
                    notes = input(' Enter any notes: ')
                    entry_list[entry_number][3] = notes
                    clear()

                with open('tasks.csv', 'w', newline='') as csvfile:
                    for entry in entry_list:
                        csvfile.write(entry[0]+','+entry[1]+','+str(entry[2])+','+entry[3])
                        csvfile.write('\n')
                break

        def delete_entry(total_entries):
            header('Delete an Entry')
            classes.DisplayEntries('tasks.csv').ShowAll()
            entry_number = int(input('\n Select an entry to delete: ')) - 1
            confirm = input('\n Are you sure you want to delete? (Y)es or (N)o: ')
            try:
                if confirm[0].upper() == 'Y':
                    entry_list = []
                    with open('tasks.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                            entry_list.append(row)
                    del entry_list[entry_number]
                    with open('tasks.csv', 'w', newline='') as csvfile:
                        for entry in entry_list:
                            for item in entry:
                                csvfile.write(item + ',')
                            csvfile.write('\n')
                else:
                    pass
            except IndexError:
                return 'Invalid selection.'


        status_message = None
        if has_entries:
            header('All Entries')
            total_entries = classes.DisplayEntries('tasks.csv').ShowAll()
            if total_entries == 0:
                status_message = 'You don\'t have any entries added!'
            menu_options = ['Edit an Entry', 'Delete an Entry']
            menu_choice = display_menu(status_message, menu_options, False)
            if menu_choice == "1":
                edit_entry(total_entries)
            elif menu_choice == "2":
                delete_entry(total_entries)
            elif menu_choice == "3":
                pass
            elif menu_choice == "4":
                clear()
                quit()
            else:
                status_message = '\n I\'m sorry that\'s not a valid option'
        else:
            return 'You don\'t have any entries added!'


    # Run the 'add entry' function if user selects it from the main menu.
    def add_entry():
        header('Add a Task')
        while True:
            try:
                task_date = datetime.datetime.strptime(input('\n Enter task date as MM/DD/YYYY: '), '%m/%d/%Y')
                task_date = task_date.strftime('%m/%d/%Y')
                break
            except ValueError:
                header('Add a Task')
                print('\n Please enter a valid date.')
        task_name = input('\n What is the task name?: ')
        while len(task_name) > 40:
            header('Add a Task')
            print('\n Enter task date as MM/DD/YYYY: {}'.format(task_date))
            task_name = input('\n I\'m sorry your task name is too long. Try again: ')
        try:
            time_spent = input('\n How many minutes were spent on this task?: ')
            if int(time_spent) > 999:
                raise ValueError
        except ValueError:
            header('Add a Task')
            print('\n Enter task date as MM/DD/YYYY: {}'.format(task_date))
            print('\n What is the task name?: {}'.format(task_name))
            return '\n Minutes spent must be an integer less than 1,000. Try again: '


        print('\n-----------(Optional)-----------')
        notes = input(' Enter any notes: ')
        task = classes.Task(task_date, task_name, time_spent, notes)
        task.write_to_file()
        clear()
        return "New entry was added successfully!"


    # Run the search menu if user selects it from the main menu.
    def search_menu():
        # Run the 'find  by date' function if user selects it from the main menu.
        def find_by_date():
            fmt = '%m/%d/%Y'
            status_message = None
            header('Find by Date')
            while True:
                try:
                    date_search = datetime.datetime.strptime(input('\n Enter a date with format MM/DD/YYYY: '), '%m/%d/%Y')
                    classes.DisplayEntries('tasks.csv').FindByDate(date_search)
                    while True:
                        menu_options = ['Return to Search']
                        menu_choice = display_menu(status_message, menu_options, False)
                        if menu_choice == '1':
                            return 'search'
                        elif menu_choice == '2':
                            return 'main'
                        elif menu_choice == '3':
                            clear()
                            quit()
                        else:
                            status_message = 'I\'m sorry that\'s not a valid option'
                            header('Find by Date')
                except ValueError:
                    header('Find by Date')
                    print('\n Please enter a valid date.')


        # Run the 'find by time spent' function if user selects it from the search menu.
        def find_by_time():
            header('Find by Time')
            time_search = input('\n Enter a number of minutes to search for: ')
            status_message = None
            classes.DisplayEntries('tasks.csv').FindByTime(time_search)
            while True:
                menu_options = ['Return to Search']
                menu_choice = display_menu(status_message, menu_options, False)
                if menu_choice == '1':
                    return 'search'
                elif menu_choice == '2':
                    return 'main'
                elif menu_choice == '3':
                    clear()
                    quit()
                else:
                    status_message = 'I\'m sorry that\'s not a valid option'
                    header('Find by Time')


        # Run the 'find by exact match' function if user selects it from the search menu.
        def find_by_exact():
            header('Find by Exact Name')
            exact_search = input('\n Enter the task name to search for: ').lower()
            status_message = None
            classes.DisplayEntries('tasks.csv').FindByExact(exact_search)
            menu_options = ['Return to Search']
            menu_choice = display_menu(status_message, menu_options, False)
            if menu_choice == '1':
                return 'search'
            elif menu_choice == '2':
                return 'main'
            elif menu_choice == '3':
                clear()
                quit()

        # Run the 'find by pattern' function if user selects it from the search menu.
        def find_by_pattern():
            status_message = None
            header('Find by Pattern')
            while True:
                regex_search = input('\n Enter a regex pattern to search: ')
                try:
                    classes.DisplayEntries('tasks.csv').FindByPattern(regex_search)
                except:
                    pass
                menu_options = ['Return to Search']
                menu_choice = display_menu(status_message, menu_options, False)
                if menu_choice == '1':
                    return 'search'
                elif menu_choice == '2':
                    return 'main'
                elif menu_choice == '3':
                    clear()
                    quit()
                else:
                    print('I\'m sorry that\'s not a valid option')


        status_message = None
        while True:
            header('Search Entries')
            menu_options = ['Find By Date', 'Find By Time Spent', 'Find By Exact Name', 'Find By Regex Pattern']
            menu_choice = display_menu(
            status_message,
            menu_options,
            False)
            if menu_choice == "1":
                clear()
                flow_control = find_by_date()
                if flow_control == 'search':
                    continue
                else:
                    break
            if menu_choice == "2":
                flow_control = find_by_time()
                if flow_control == 'search':
                    continue
                else:
                    break
            if menu_choice == "3":
                flow_control = find_by_exact()
                if flow_control == 'search':
                    continue
                else:
                    break
            if menu_choice == "4":
                flow_control = find_by_pattern()
                if flow_control == 'search':
                    continue
                else:
                    break
            if menu_choice == "5":
                clear()
                break
            elif menu_choice == "6":
                clear()
                break
            else:
                status_message = 'I\'m sorry that\'s not a valid option'

    # Clears the console screen when function is called between menu changes.
    def clear():
        os.system("cls" if os.name == "nt" else "clear")


    def display_menu(status_message, menu_options, is_main_menu):
        if is_main_menu:
            classes.MainMenu(status_message, menu_options)
        else:
            classes.Menu(status_message, menu_options)
        return menu_prompt()

    while True:
        header('Work Log')
        menu_options = ['Add New Entry', 'Modify Entries', 'Search Entries']
        menu_choice = display_menu(
            status_message,
            menu_options,
            True)
        if menu_choice == "1":
            status_message = add_entry()
            continue
        elif menu_choice == "2":
            status_message = modify_entries()
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
