from random import randint
from time import sleep

import concurrent.futures


def do_job(num):
    sleep_sec = randint(1, 3)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    sleep(sleep_sec)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as worker:
    for num in range(10):
        print('#%d Worker initialization' % num)
        worker.submit(do_job, num)
