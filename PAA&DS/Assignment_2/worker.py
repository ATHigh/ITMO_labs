from mpi4py import MPI

comm = MPI.Comm.Get_parent()
rank = comm.Get_rank()
print(f"Create worker with rank {rank}")
comm.send(rank, dest=0, tag=rank)
comm.Disconnect()