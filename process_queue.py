# -*- coding: UTF-8 -*-
# 多进程 生产者/消费者


import multiprocessing as mp


def consumer(input_q):
    while True:
        item = input_q.get()
        input_q.task_done()
        print 'consume'+item


def producer(sequence, output_q):
    for item in sequence:
        print 'produce'+item
        output_q.put(item)


obj = ['1', '2', '3', '4', '5']

test_queue = mp.JoinableQueue()
test_pro = mp.Process(target=consumer, args=(test_queue,))
test_pro.daemon = True
test_pro.start()

producer(obj, test_queue)
test_queue.join()







