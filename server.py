"""
    Adapted from:
        https://docs.python.org/2/library/multiprocessing.html#using-a-remote-manager
"""

from multiprocessing.managers import BaseManager
import Queue

queue = Queue.Queue()
BaseManager.register('get_queue', callable=lambda:queue)
m = BaseManager(address=('', 50000), authkey='password')
s = m.get_server()
s.serve_forever()