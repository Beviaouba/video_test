import multiprocessing

bind = '127.0.0.1:8001'
workers = multiprocessing.cpu_count() * 2 - 1
workers_class = 'gevent'