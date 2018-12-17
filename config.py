bind = '%s:%s' % ('127.0.0.1', '8080')
workers = 1


def post_fork(server, worker):
    """Allocate ~100MB of integers"""
    print('post_fork', worker.pid)
    items = list(range(4300800))


def worker_int(worker):
    print('worker_int', worker.pid)


def child_exit(server, worker):
    print('child_exit', worker.pid)


def worker_abort(worker):
    print('worker_abort', worker.pid)
