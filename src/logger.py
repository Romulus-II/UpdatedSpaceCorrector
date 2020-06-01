import datetime

class Logger:
    def __init__(self, os):
        self.time_created = datetime.datetime.now()
        time_created = str(self.time_created)
        time_created = time_created.replace(':','.')
        self.file_name = ('data/logs/' + time_created + '.txt')
        print('Saving corrections under ' + self.file_name)
        self.file = open(self.file_name, "w")
        self.file.close()

    def write(string):
        self.file.write(string)

    def write_line(line):
        self.file.write_line(line)

    def publish():
        self.file.close()
