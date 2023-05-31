#=====================================
# Recursividad y memorización 
#=====================================

#=====================================
# Herraminetas para la memorización
#=====================================
from functools import lru_cache

def fibonnaci_lento(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fibonnaci_lento(n-1)+fibonnaci_lento(n-2)


for i in range(1,36):
    print(str(i)+ ":", fibonnaci_lento(i))

#============================================
# Optimizacion 2: uso de conjuntos para
#                 guardar valores 
#============================================

#===============================
# Conjunto de fibonnacis
#===============================
fibonnacis = {}
def fibonnaci(n):
    
    #=========================================
    # Revisa si ya existe y regresa el valor
    #=========================================
    if n in fibonnacis:
        return fibonnacis[n]
    
    if n ==1:
        valor = 1
    elif n==2:
        valor=1
    elif n>2:
        valor = fibonnaci(n-1)+ fibonnaci(n-2)
        
    #====================
    # Guardalo
    #====================
    fibonnacis[n] = valor
    return valor

for i in range(1, 10001):
    print(str(i)+":",fibonnaci(i))

#========================================
# Uso de decoradores para memorizacion 
# maxsize: es cuantos anteriores guarde
#========================================
@lru_cache(maxsize=3)
def nfibonnaci(n):
    if type(n)!=int:
        raise TypeError("n debe ser entero positivo")
    if n<1:
        raise ValueError("n debe ser entero positivo")
        
    if n==1:
        return 1
    if n==2:
        return 2
    elif n>2:
        return nfibonnaci(n-1)+nfibonnaci(n-2)

for i in range(1,10001):
    print(str(i)+":",nfibonnaci(i))
    
    
    
    
    
    
    
    
    
    
    
    
    
    