# Best run via dedicated term


import time
from multiprocessing import shared_memory, Process, freeze_support, set_start_method
import os

import psutil
import numpy as np
from humanize import naturalsize

#
# Make a big array
# E.g., analagously, this could be a large ML model we want to serve

array_n = 10**4
big_matrix = np.random.rand(array_n, array_n)

print("array size: ", naturalsize(big_matrix.nbytes))

#
# Worker func. Run on forked process
def worker_func(worker_number, matrix):
    for _ in range(100):
        print(f"I'm worker {worker_number} with a {matrix.shape[0]}x{matrix.shape[1]} matrix summing to {matrix.sum()}")
        time.sleep(10)


#
# Spawn some processes
if __name__ == "__main__":
    freeze_support()
    set_start_method("fork")

    parent_pid = os.getpid()

    processes = []
    worker_number = 0
    while True:
        print(f"about to fork a proces. will create worker {worker_number}")
        input()

        proc = Process(target=worker_func, args=[worker_number, big_matrix])
        processes.append(proc)
        proc.start()

        # print("RSS", naturalsize(psutil.Process(parent_pid).memory_info().rss))
        # print("VMS", naturalsize(psutil.Process(parent_pid).memory_info().vms))

        worker_number += 1
