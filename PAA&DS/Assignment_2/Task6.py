from mpi4py import MPI
from sys import getsizeof
import time
import numpy as np

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

N = 10

if rank == 0:
    for i in range(51):
        array = np.random.randint(0, 100, size=10000 * i)
        L = getsizeof(array)
        start = time.time()
        for j in range(N):
            MPI.COMM_WORLD.send(array, dest=1, tag=0)
            array = MPI.COMM_WORLD.recv(source=1, tag=0)

        execution_time = time.time() - start
        R = ((2 * N * L) / execution_time) / 1024**2
        print(f'Object_size {L} (bytes): {round(R, 2)} (MB/s)')

if rank == 1:
    for i in range(51):
        for j in range(N):
            m = MPI.COMM_WORLD.recv(source=0, tag=0)
            MPI.COMM_WORLD.send(m, dest=0, tag=0)
