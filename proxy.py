# -*- coding: UTF-8 -*-
# 场景: 如果工人不忙,代理通知工人去工作


class Worker:
    def work(self):
        print 'i am working'


class Proxy:
    def __init__(self):
        self.busy = 'no'
        self.worker = None

    def work(self):
        if self.busy == 'no':
            self.worker = Worker()
            self.worker.work()

        else:
            print 'he is busy'


p = Proxy()
p.work()
