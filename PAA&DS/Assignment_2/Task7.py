from mpi4py import MPI

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

if rank == 0:
    message = f'Rank {rank} sent to {rank + 1}'
    MPI.COMM_WORLD.send(message, dest=1, tag=1)
    message = MPI.COMM_WORLD.recv(source=size-1, tag=0)
    print(f'DONE, get - {message}')

else:
    source = rank-1
    message = MPI.COMM_WORLD.recv(source=source, tag=rank)
    print(f'Worker {rank} received the message - {message}')

    destination = (rank + 1) % size
    message = f'Rank {rank} sent to {destination}'
    print(f'Worker {rank} sent the message - {message}')
    MPI.COMM_WORLD.send(message, dest=destination, tag=destination)
