#====================================
# PROGRAMACIÓN ORIENTADA A OBJETOS
#====================================

#================================
# Una clase para un objeto vacío
# No está vacío, necesita 
# la palabra pass = pasar
#================================
class ObjetoVacio:
    pass

#========================
# nada es un ObjetoVacio
#========================
nada = ObjetoVacio()
print(type(nada))

#==================
# La clase llanta 
#==================
class Llanta:
    #--------------------------------------
    # Variable cuenta es de toda la clase 
    #--------------------------------------
    cuenta = 0
    #=====================================
    # Funcion constructora de indentidad
    # _init_ es una funcion reservada
    # comienza con uno mismo: self
    # pero puede ser otro nombre (mi)
    # parametros de entrada = default
    #=====================================
    
    def __init__(mi, radio=50, ancho=30, presion=1.5):
        # Variable de la etructura completa Llanta
        Llanta.cuenta += 1
        # Variables exlcusivas  de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion
        
#===============================
# Objetos (instanciados)
#===============================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#===================================
# Objeto que contiene otros objetos
#===================================
class Coche:
    def __init__(mi,ll1, ll2, ll3, ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4
        
micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta) #Variable global de la clase
print("Presion de la llanta 4 = ", llanta4.presion)
print("Radio de la llanta 4 = ", llanta4.radio)
print("Presion de la llanta 1 de mi coche = ", micoche.llanta1.presion)

    
#===================
# Encapsulamieto
#===================

#====================================================================
# Uso de la funcion de python property para poner y obtener atributos
#====================================================================
class Estudiante:
    def __init__(mi):
        mi._nombre = ''
        def poner_nombre(mi,nombre):
            print('se llamo a poner_nombre')
            mi._nombre=nombre
        def obtener_nombre(mi):
            print('se llamo a obtener_nombre')
            return mi._nombre
        nombre=property(obtener_nombre, poner_nombre)
    
#====================================
# Crear objeto estudiante sin nombre
#====================================
estudiante = Estudiante()

#==================================================================
# Poner nombre usando la propiedad nombre y el metodo poner_nombre
# (sin tener que llamar explicitamente la funcion)
#==================================================================    
estudiante.nombre = "Stark"

#==================================================================
# Obtener el nombre con el metodo obtener_nombre
# _nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explicitamente a la funcion obtener_nombre)
#==================================================================
print(estudiante.nombre)

# Esto no funciona
#print(estudiante._nombre)

#==========================
# Herencia de clases
#==========================

class Cuadrilatero:
    def __init__(mi,a,b,c,d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d
        
    def perimetro(mi):
        p=mi.lado1+mi.lado2+mi.lado4+mi.lado3
        print("perimetro=",p)
        return p

#===================================
# Su hijo rectangulo 
# Rectangulo es hijo de Cuadrilatero
# Rectangulo(Cuadrilatero)
#===================================
class Rectangulo(Cuadrilatero):
    def __init__(self, a,b):
    #=========================
    # Constructor de su madre
    #=========================
        super().__init__(a,b,a,b)
    
#=======================
# Su nieto Cuadrado
# Hijo de Rectangulo
#=======================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)
        
    def area(self):
        area = self.lado1**2
        return area
    '''   
    def perimetro(self):
        p=4.0*self.lado1
        print("perimetro = ",p)
        return p
    '''

#==================
# Crear un Cuadrado
#==================
cuadrado1=Cuadrado(5)

#======================================================
# Llamar al metodo perimetro de su abuelo Cuadrilatero
#======================================================
perimetro1 = cuadrado1.perimetro()

#===========================================
# Llamar a su propio metodo area
#===========================================
area1=cuadrado1.area()

print("perimetro = ", perimetro1)
print("area = ", area1)

#===============================================================
# Sobre-escribir un metodo de su madre o abuela o tatarabuela...
# Es volver a definir una funcion ya existenete
#===============================================================

#+++++++++++++++++++++++++++++++++
#          ASOCIACION
#+++++++++++++++++++++++++++++++++

#=====================================
# La clase A tiene tres numero reales
#=====================================
class A:
    _a:float=0.0
    _b:float=0.0
    _c:float=0.0
    
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c
        
#====================================
# La clase B tiene dos numeros reales
#====================================

class B:
    _d:float
    _e:float
    
    def __init__(self,d:float, e:float):
        self.d=d
        self.e=e
        
    #========================================
    # Metodo sumar todo (internos + externos)
    #========================================
    def sumar_todo(self, aa:float, bb:float):
        x=float=self.d+self.e+aa+bb
        return x

#============
# ASOCIACION
#============
# Usando objetos independientes
objetoA = A(1.0,2.0, 3.0)
objetoB = B(4.0,5.0)
print(objetoB.sumar_todo(objetoA.a, objetoA.b))

#=============================================
# El objeto C tiene dos reales y un objeto A
# El objeto A se instancia dentro de C
#=============================================
class C:
    _d:float=0.0
    _e:float=0.0
    _Aa:A=None
    
    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return x
    
#=============================
# COMPOSICION
# Contiene toro objeto dentro
#=============================
class D:
    _d:float=0.0
    _e:float=0.0
    _Aa:A=None
    
    def __init__(self,d:float,e:float,Aa:A):
        self.d=d
        self.e=e
        self.Aa=Aa
    
    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return x
        
#========================================
# AGREGACION
# Construye el objeto agregado por fuera
#========================================
objetoD = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())
        


    