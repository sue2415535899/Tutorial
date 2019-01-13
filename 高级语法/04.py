#enclding=utf-8
import threading
import time
#Python 2
#from Quene import Quene

#python 3
import queue
class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True :
            if queue.qsize() <1000:
                for i in range(100):
                    count += 1
                    msg= "生成产品"+str(count)
                    #往队列queue中放一个东西
                    queue.put(msg)
                    print (msg )
            time.sleep(0.5)
class Consumer(threading.Thread):
    def run(self):
        global queue
        while True :
            if queue.qsize() >100:
                for i in range(3):
                    #从队列queue中拿出一条消息
                    msg= self.name+'消费了'+queue.get()
                    print (msg )
            time.sleep(1)
if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(500):
        queue.put('初始产品'+str(i))
    for i in range (2):
        p = Producer()
        p.start()
    for i in range (5):
        c = Consumer()
        c.start()