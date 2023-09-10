import time


class log:
    def __init__(self, file, mode='r'):
        self.opened_file = file
        self.mode = mode

    def __enter__(self):
        file = open(self.opened_file, self.mode)
        started = time.asctime(time.localtime(time.time()))
        print(started)
        time.sleep(2)
        return file

    def __exit__(self, exc_type, exc_val, exc_tb):
        file.close()
        fnished = time.asctime(time.localtime(time.time()))
        print(fnished)


with log("task.txt", 'w') as file:
    file.write('hello')

