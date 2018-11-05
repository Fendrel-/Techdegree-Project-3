import csv
import datetime


class Menu(list):
    def __init__(self, status_message, menu_options):
        self.extend(menu_options)
        if status_message:
            print('\n ' + status_message)
        print('')
        for count, item in enumerate(self, start=1):
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
    def __init__(self, status_message, menu_options):
        self.extend(menu_options)
        if status_message:
            print('\n ' + status_message)
        print('')
        for count, item in enumerate(self, start=1):
            print(' [{}] {}'.format(count, item))
        print('')
        count += 1
        print(' [{}] Quit'.format(count))


class Task():
    def __init__(self, task_date, name, minutes, notes):
        self.task_date = task_date
        self.name = name
        self.minutes = minutes
        self.notes = notes

    def write_to_file(self):
        with open('tasks.csv', 'a') as csvfile:
            csvfile.write(self.task_date + ',' + self.name + ',' + self.minutes + ',' + self.notes + '\n')

class DisplayEntries():
    def __init__(self, filename):
        self.filename = filename

    def ShowAll(self):
        try:
            with open(self.filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                col1_width = 13
                col2_width = max([len(row[1]) for row in reader]) + 3
                col3_width = 10
                csvfile.seek(0)
                col4_width = max([len(row[3]) for row in reader])
                print('\n     Date' + ' ' * (col1_width - 10), end="")
                print('Task' + ' ' * (col2_width - 4), end="")
                print('Minutes' + ' ' * (col3_width - 7), end="")
                print('Notes', end="")
                print('\n ', end="")
                print('-' * (col1_width + col2_width + col3_width + col4_width + 4))

                csvfile.seek(0)
                count = 0
                for row in reader:
                    count += 1
                    print(' {}  '.format(count), end="")
                    print(' ' + row[0] + ' ' * (col1_width - len(row[0])), end="")
                    print(row[1] + ' ' * (col2_width - len(row[1])), end="")
                    print(row[2] + ' ' * (col3_width - len(row[2])), end="")
                    print(row[3])
                if count == 1:
                    print('\n\n 1 entry found.')
                else:
                    print('\n\n {} entries found.'.format(count))
            return True
        except (IndexError, ValueError):
            return False

    def FindByDate(self, date_search):
        try:
            with open(self.filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                col1_width = 13
                col2_width = max([len(row[1]) for row in reader]) + 3
                col3_width = 10
                csvfile.seek(0)
                col4_width = max([len(row[3]) for row in reader])
                print('\n     Date Added' + ' ' * (col1_width - 10), end="")
                print('Task' + ' ' * (col2_width - 4), end="")
                print('Minutes' + ' ' * (col3_width - 7), end="")
                print('Notes', end="")
                print('\n ', end="")
                print('-' * (col1_width + col2_width + col3_width + col4_width + 4))
                csvfile.seek(0)
                count = 0
                for row in reader:
                    if datetime.datetime.strptime(row[0], '%m/%d/%Y') == date_search:
                        count += 1
                        print(' {}  '.format(count), end='')
                        print(' ' + row[0] + ' ' * (col1_width - len(row[0])), end="")
                        print(row[1] + ' ' * (col2_width - len(row[1])), end="")
                        print(row[2] + ' ' * (col3_width - len(row[2])), end="")
                        print(row[3])
                if count == 1:
                    print('\n\n 1 entry found.')
                else:
                    print('\n {} entries found.'.format(count))
            return True
        except (IndexError, ValueError):
            return False

    def FindByTime(self, time_search):
        try:
            with open(self.filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                col1_width = 13
                col2_width = max([len(row[1]) for row in reader]) + 3
                col3_width = 10
                csvfile.seek(0)
                col4_width = max([len(row[3]) for row in reader])
                print('\n     Date Added' + ' ' * (col1_width - 10), end="")
                print('Task' + ' ' * (col2_width - 4), end="")
                print('Minutes' + ' ' * (col3_width - 7), end="")
                print('Notes', end="")
                print('\n ', end="")
                print('-' * (col1_width + col2_width + col3_width + col4_width + 4))
                csvfile.seek(0)
                count = 0
                for row in reader:
                    if row[2] == time_search:
                        count += 1
                        print(' {}  '.format(count), end='')
                        print(' ' + row[0] + ' ' * (col1_width - len(row[0])), end="")
                        print(row[1] + ' ' * (col2_width - len(row[1])), end="")
                        print(row[2] + ' ' * (col3_width - len(row[2])), end="")
                        print(row[3])
                if count == 1:
                    print('\n\n 1 entry found.')
                else:
                    print('\n {} entries found.'.format(count))
            return True
        except (IndexError, ValueError):
            return False
