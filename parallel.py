'''
The easy way to do parallel threads or processes.
'''

import time
import random
import itertools
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool


def io_bound(x):
    'simualte and input/output-constrainded task'
    time.sleep(random.random()*2)
    return x + 1

def cpu_bound(x):
    'a compute-constrained task'
    sum(xrange(int(1e8)))
    return x + 1


def serial(func, n):
    for result in itertools.imap(io_bound, xrange(n)):
        print result


def threaded(func, n):
    pool = ThreadPool(n/4)
    for result in pool.imap_unordered(func, xrange(n)):
        print result


def multiproc(func, n):
    pool = Pool(n)
    for result in pool.imap_unordered(func, xrange(n)):
        print result

        
if __name__ == '__main__':
    start = time.time()
    multiproc(cpu_bound, 10)
    stop = time.time()
    print 'DURATION:', stop-start
    
