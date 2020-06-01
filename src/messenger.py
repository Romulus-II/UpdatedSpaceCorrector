class Messenger:
    def __init__(self):
        self.split_count = 0

    def convert_answer(self, ans):
        if 'y' in ans or 'Y' in ans:
            return True
        else:
            return False

    def prompt(self):
        if self.split_count == 0:
            return input('Would you like to split a line? ')
        else:
            return input('Would you like to split another line? ')

    def collect_input(self):
        self.split_count += 1
        return input('Enter line to split: \n')
