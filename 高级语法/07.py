from  multiprocessing import Process
from time import sleep ,ctime
import os
def info(title):
    print(title)
    print('module name :',__name__ )
    #主进程id
    print('parent process :',os.getppid())
    #自己的id
    print('process_id:',os.getpid())

def f(name) :
    info('function f')
    print ('hello ',name )

if __name__ == '__main__':
    info('main line ')
    p = Process(target=f,args =('bob',))
    p.start()
    p.join()