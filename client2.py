"""
    Adapted from:
        https://docs.python.org/2/library/multiprocessing.html#using-a-remote-manager
"""

from multiprocessing.managers import BaseManager

BaseManager.register('get_queue')
m = BaseManager(address=('127.0.0.1', 50000), authkey='password')
m.connect()
queue = m.get_queue()
print queue.get()