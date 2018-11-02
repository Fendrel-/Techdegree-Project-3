import os


class Header():
    def __init(self, name):
        self.name = name
        print('-' * 35)
        print(' ' + self.name)
        print('-' * 35)

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
        self.count = count


class MainMenu(Menu):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.count += 1
        print(' [{}] Quit'.format(self.count))
