import sys


bind = '%s:%s' % ('127.0.0.1', '8080')
workers = 1


def post_fork(server, worker):
    """Allocate ~100MB of integers"""
    print('post_fork', worker.pid)
    intsize = sys.getsizeof(int())
    KB = 1024 // intsize
    MB = 1024 * KB
    items = list(range(100 * MB))


def child_exit(server, worker):
    print('child_exit', worker.pid)
