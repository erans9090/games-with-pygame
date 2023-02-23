import datetime


class Logger:

    def __init__(self):


        self.log_file = f'logs\\log--{datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")}.txt'

        with open(self.log_file, 'w+') as f:
            pass

    def log(self, message):

        with open(self.log_file, 'a') as f:

            f.write(message + '\n')

    