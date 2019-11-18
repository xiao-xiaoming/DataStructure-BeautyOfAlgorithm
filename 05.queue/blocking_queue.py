# -*- coding: utf-8 -*-
__author__ = 'xiaoxiaoming'

import queue
import random
import threading
import time


class Producer(threading.Thread):
    nameList = ["apple", "peach", "pineapple", "orange", "banana", "blueberry"]
    flag = 1

    def __init__(self, q, name):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        name_list = Producer.nameList
        while Producer.flag:
            queueLock.acquire()
            if not self.q.full():
                data = name_list[random.randrange(0, len(name_list))]
                self.q.put(data)
                print("%s 生产数据: %s" % (threading.currentThread().name, data))
                queueLock.release()
            else:
                queueLock.release()
            time.sleep(random.random() * 3)


class Consumer(threading.Thread):
    flag = 1

    def __init__(self, q, name):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        while Consumer.flag:
            queueLock.acquire()
            if not self.q.is_empty():
                data = self.q.get()
                print("%s 消费数据: %s" % (threading.currentThread().name, data))
                queueLock.release()
            else:
                queueLock.release()
            time.sleep(random.random() * 4)


workQueue = queue.Queue(5)
queueLock = threading.Lock()
# 创建新线程
Producer(workQueue, "Producer1").start()
Producer(workQueue, "Producer2").start()
Consumer(workQueue, "Consumer1").start()
Consumer(workQueue, "Consumer2").start()
Consumer(workQueue, "Consumer3").start()

while 1:
    time.sleep(1)
    print(workQueue.queue)