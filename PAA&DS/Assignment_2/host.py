from mpi4py import MPI
import sys

size = 3
comm = MPI.COMM_WORLD.Spawn(sys.executable, args=['worker.py'], maxprocs=size)

for i in range(size):
    data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG)
    print(f"Received message from worker {data}")

comm.Disconnect()
