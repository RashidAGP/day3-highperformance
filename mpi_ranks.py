from mpi4py import MPI
import numpy
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 4

result = 0


if rank == 0:
    print("Process" + str(rank) + "\n")
    data = comm.Recv(rank,src = MPI.ANY_SOURCE)
    result += data
else:
    print("Process" + str(rank) + "\n")
    comm.Send(rank, dest=0)



if rank == 0:
    print("The final result is : " + str(data))
