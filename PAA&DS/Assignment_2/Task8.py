from mpi4py import MPI
import time
import datetime

rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

if rank == 0:
    print(f'{datetime.datetime.now().time()}\tHost sent message to worker (host_message)')
    req = MPI.COMM_WORLD.isend("host_message", dest=1, tag=0)
    req.wait()

    for i in range(5):
        time.sleep(5)
        print(f"{datetime.datetime.now().time()}\tWAITING")

    req = MPI.COMM_WORLD.irecv(source=1, tag=1)
    print(f"{datetime.datetime.now().time()}\tHost received message from worker ({req.wait()})")

if rank == 1:
    req = MPI.COMM_WORLD.irecv(source=0, tag=0)
    print(f"{datetime.datetime.now().time()}\tWorker {rank} received message from host ({req.wait()})")

    print(f"{datetime.datetime.now().time()}\tWorker {rank} sent message to host (worker_message)")
    req = MPI.COMM_WORLD.isend("worker_message", dest=0, tag=1)
    req.wait()