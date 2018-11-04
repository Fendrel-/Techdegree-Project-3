class Menu(list):
    def __init__(self, message, *args, **kwargs):
        for item in args:
            self.append(item)
        if message:
            print('\n ' + message)
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
    def __init__(self, message, *args, **kwargs):
        for item in args:
            self.append(item)
        if message:
            print('\n ' + message)
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
