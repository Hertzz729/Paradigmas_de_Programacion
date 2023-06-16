#================================================
# Uso de MPI optimizado para calculos numericos
#================================================
from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self,rank):
        #=======================================
        # Arreglo de numpy (optimizado)
        #=======================================
        self.x = np.array([float(x+rank) for x in range(10)])
        self.p = "vengo del proceso "+str(rank)

#========================
# Programa principál
#========================
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size -1
    dst = rank+1 if rank!= size-1 else 0

    #===============================
    # Arreglo para enviar 
    #===============================
    m = s.x
    #print(m)
    #=========================================
    # Isend Irecv son para comunicacion 
    # no bloqueante de arreglos de numpy
    #=========================================
    comm.Isend(m, dest=dst)

    #=================================================
    # Arreglo vacio para recibir 
    # con dimension 10 y tipo de datos
    # float (doble precision)
    #=================================================
    a = np.zeros(10, dtype=no.float64)
    req = comm.Irecv(a, source =src)
    req.wait()
    
    print("Soy el proceso ", rankm ", el resultado es ", a )

