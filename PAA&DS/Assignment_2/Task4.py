from mpi4py import MPI
import time

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()


if rank == 0:
    time.sleep(3)

    req = MPI.COMM_WORLD.irecv(source=1, tag=0)
    message = req.wait()

    print(f'Host got message {(time.time() - message):.2f} seconds ago')

if rank == 1:
    message = time.time()
    req = MPI.COMM_WORLD.isend(message, dest=0, tag=0)
    req.wait()
    for sec in range(1, 11):
        print(f'Worker works {sec} seconds')
        time.sleep(3)
