from mpi4py import MPI
import numpy as np

# Get my rank
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()

class class_object:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def production(self):
        return (self.a + self.b) / self.c

    def __str__(self):
        return f"a = {self.a} b = {self.b} c = {self.c} production = {round(self.production(), 2)}"

# fill the missing part
object1 = list(range(10))
object2 = class_object(np.random.randint(50), np.random.randint(50), np.random.randint(50))
object3 = np.random.randint(0, 100, 5)

list_of_objects = [object1, object2, object3]

if rank == 0:
    data = list_of_objects
else:
    data = None

data = MPI.COMM_WORLD.scatter(data, root=0)
print(f"In rank {rank} there is data:\n{data}")