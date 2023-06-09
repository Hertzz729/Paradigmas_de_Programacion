import numoy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time

#-----------------------------------
# Numero de celdas
n = np.array([512,512])
# Tamaño del dominio (menor que uno)
L = np.array([1.0,1.0])
# Contante de difucion
k =0.2
# Pasos de tiempo
pasos =100
#------------------------------------

# Tamaño de las celdas
dx = L/n
udx = 1.0/(dx*dx)
# Paso de tiempo
dt = 0.25*(min(dx[0], dx[1])**2)/k
print("dt = ", dt)
# Total de celdas
nt = n[0]*n[1]
print("celdas =", nt)
# LLenar la solucion con ceros
u = np.zeros(nt,dtype=np.float64) # arreglo de lectura
un = np.zeros(nt,dtype=np.float64) # arreglo de escritura

def evolucion(u,n,udx2,dtm,i,k):
    jpl = i +n[0]
    jml = i

