import multiprocessing
from time import sleep,ctime

def consumer(input_q):
    print("Into consumer :",ctime())
    while True :
        item = input_q.get()
        if item is None:
            break
        print("pull",item,"out of q")#领一个任务
        input_q.task_done() #发出信号通知信号任务完成
    print("out of consume:",ctime())#未执行
def producer(sequence,output_q):
    print ("Into procuder:",ctime())
    for item in sequence:
        output_q.put(item)
        print("put ",item ,"into q ")
    print ("out of procuder:",ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    cons_p =  multiprocessing.Process(target = consumer,args = (q,))
    cons_p.daemon = True#守护进程
    cons_p.start()

    #生产多个项，sequence 代表要发给消费者的项序列
    #在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence,q)
    #等待所有项被处理
    q.put(None)
    cons_p.join()

