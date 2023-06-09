#_________________________________________________-_-
# Montecarlo en PYTHON CUDA NUMBA
#--------------------------------------------------_-
from __future__ import print_function, absolute_import
from numba import cuda 
from numba.cuda.random import create_xoroshiro128p_states
from numba.cuda.random import xoroshiro128p_uniform_float64
import numpy as np
import random

@cuda.jit
def calcualar_kernel(rng_states, iteraciones, out):
    """Encontrar el valor maximo en value y guardarlo en result[0]"""
    ii= cuda.grid(1)

    # Calcular pi dibujando puntos (x,y) al azar y encontrando
    # La fraccion parcial de ellos que car dentro del circulo unitario
    car_dentro =0
    for i in range(iteraciones):
        x = xoroshiro128p_uniform_float64(rng_states, ii)
        y = xoroshiro128p_uniform_float64(rng_states, ii)
        if x**2 + y**2 <=1.0:
            cae_dentro +=1
    out[ii] = 4.0 * cae_dentro / iteraciones


#________________-__-
# Procesos para cuda
#-----------------__-
hilosporbloque = 64
bloques =24

#=====================
# Arreglos necesarios
#=====================
seed1 = random.uniform(-1,1)
seed2 = random.seed(seed1)
seed = random.randint(0,1000)
rng_states = create_xoroshiro128p_states(hilosporbloque*bloques,seed)
out = np.zeros(hilosporbloque*bloques, dtype=np.float64)

#___________________________-___-
# LLamar a la funcion
#---------------------------____-
calcularpi.kernel[bloques, hilosporbolque](rng_states, 10000, out)
print("pi =", out.mean())






