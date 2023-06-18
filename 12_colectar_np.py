from mpi4py import MPI
import numpy 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 10

#===========================================
# Arreglo de ceros de tamaño n
# sumando con un escalor (en cada entrada)
#===========================================
sendarray = numpy.zeros(n,dtype="i")+rank

recvarray = None

if rank == 0:
    #====================================
    # Matriz vacia de tamaño procesos *n
    # dtype es el tipo de dato (i) es entero
    #=======================================

#==================================
# Gather es rapido para numpy
# enviar datos al proceso root 
#==================================
comm:Gather(sendarray, recvarray, root=0)

if rank ==0:
    for i in range(size):
        #==========================================================
        # revisar por fila la matriz 
        # : significa todos los elementos de esa dimension
        # allclose es un metodo de numpy que compara los elementos
        #==========================================================
        assert numpy.allclose(recvarray[i,:], i)
        
print(recvarray)
        
    
    
    
    
    
    
    
    
    