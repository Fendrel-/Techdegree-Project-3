import os

class Menu(list):
    def __init__(self, name=None, *args, **kwargs):
        os.system('cls')
        self.name = name
        for item in args:
            self.append(item)
        print('-' * 35)
        print(' ' + self.name)
        print('-' * 35)

    def prompt(self):
        for count,item in enumerate(self, start=1):
            print('[{}] {}'.format(count, item))

        print('[{}] Quit'.format(count+1))
        choice = input('\nChoose an option: ')
        return choice

class Add(Menu):
    pass
