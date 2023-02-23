import datetime
import os
        
class Logger:

    def __init__(self):
        log_dir = 'snake/logs'

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self.log_file = f'{log_dir}/log--{datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")}.txt'

        with open(self.log_file, 'w+') as f:
            pass

    def log(self, message):

        with open(self.log_file, 'a') as f:

            f.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {message} \n")

    