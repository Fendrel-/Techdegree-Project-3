import datetime
import pytz


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
        try:
            count += 1
        except:
            count = 1
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

class Task():
    def __init__(self, name, minutes, notes):
        self.name = name
        self.minutes = minutes
        self.notes = notes

    def write_to_file(self):
        today = datetime.date.today().strftime('%m/%d/%Y')
        with open('tasks.csv', 'a') as csvfile:
            csvfile.write(today + ', ' + self.name + ', ' + self.minutes + ', '  + self.notes + '\n')
