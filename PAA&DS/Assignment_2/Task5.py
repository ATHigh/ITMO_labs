import numpy as np
from mpi4py import MPI

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

vector_1, vector_2 = np.full(100000, 1), np.full(1000000, 2)

fragment_1, fragment_2 = np.array_split(vector_1, size), np.array_split(vector_2, size)

l = []
for frag in zip(fragment_1, fragment_2):
    l.append(frag)

if rank == 0:
    data = l
else:
    data = None

data = MPI.COMM_WORLD.scatter(data, root=0)
print(f'Rank {rank} stores data: {data}')

vector_product = np.dot(*data)
receive_message = MPI.COMM_WORLD.gather(vector_product, root=0)
result = 0

if rank == 0:
    for i in range(size):
        print(f'Rank {i}, result = {receive_message[i]}')
        result += receive_message[i]


print(f'Final result = {result}')
