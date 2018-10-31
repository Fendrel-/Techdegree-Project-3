class Menu(list):
    def __init__(self, name=None, *args, **kwargs):
        self.name = name
        for item in args:
            self.append(item)

    def prompt(self):
        print('-' * 35)
        print(self.name)
        print('-' * 35)
        for count,item in enumerate(self, start=1):
            print('[{}] {}'.format(count, item))
        return input('\nChoose an option: ')
