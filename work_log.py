import os

import menu


def telepathy():
    pass

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def add_item():
    pass

def search_menu():
    clear()
    menu_screen = menu.Menu('Search Menu', 'Search By Telepathy')
    return menu_screen.prompt()

def add_menu():
    clear()
    menu_screen = menu.Menu('Add New Entry', 'New')
    return menu_screen.prompt()

def top_menu():
    clear()
    menu_screen = menu.Menu('Main Menu', 'Add New Entry', 'Lookup Entry')
    return menu_screen.prompt()

def navigation():
    current_menu = "main"
    user_input = top_menu()
    while True:
        if current_menu == "main":
            if user_input == "1":
                current_menu = "add"
                continue
            elif user_input == "2":
                current_menu = "search"
                continue

        elif current_menu == "add":
            user_input = add_menu()
            if user_input == "1":
                add_item()

        elif current_menu == "search":
            user_input = search_menu()
            if user_input == "1":
                telepathy()

if __name__ == "__main__":
    navigation()
