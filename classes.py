import os


class Menu(list):
    def __init__(self, message, *args, **kwargs):
        for item in args:
            self.append(item)
        if message:
            print('\n ' + message)
        print('')
        for count,item in enumerate(self, start=1):
            print(' [{}] {}'.format(count, item))
        print('')
        count += 1
        print(' [{}] Main Menu'.format(count))
        count += 1
        print(' [{}] Quit'.format(count))


class MainMenu(Menu):
    def __init__(self, message, *args, **kwargs):
        for item in args:
            self.append(item)
        if message:
            print('\n ' + message)
        print('')
        for count,item in enumerate(self, start=1):
            print(' [{}] {}'.format(count, item))
        print('')
        count += 1
        print(' [{}] Quit'.format(count))
