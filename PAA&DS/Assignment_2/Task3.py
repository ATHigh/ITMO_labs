from mpi4py import MPI
import time

#Get my rank
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

if rank == 0:
    for i in range(1, size):
        start_time = MPI.COMM_WORLD.recv(source=i, tag=i)
        execution_time = (time.time() - start_time) * 1000
        print(f"Worker with rank {i} got message in {execution_time:.0f} ms")
else:
    start_time = time.time()
    MPI.COMM_WORLD.send(start_time, dest=0, tag=rank)