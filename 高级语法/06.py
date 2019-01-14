import multiprocessing
from time import sleep ,ctime

class ClockProcess(multiprocessing.Process):
    '''
    init 函数
    run 函数
    '''
    def __init__(self,interval):
        super().__init__()
        self.interval = interval
    def run(self):
        while True:
            print ("the time is %s " % ctime())
            sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()