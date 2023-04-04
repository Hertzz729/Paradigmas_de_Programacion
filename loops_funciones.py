#===================
#Condicionales
#===================
precio=50
#------------
# Si esto..
#------------
if precio<50:
    print("El precio es menor que 50")
#--------------------------
# Si no.. si esto otro...
#--------------------------
elif precio > 50:
    print("El precio es mayo a 50")
#--------------------------
# Si nada de lo antrior...
#--------------------------
else:
    print("El precio es 50")
precio = 50
cantidad = 5
total = precio*cantidad
#========================
# Condicionales anidados
#========================
if total > 100:
    if total >500:
        print("Total es mayor que 500")
    else: 
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor que 400")
        elif total < 500 and total > 300:
            print("Total entre 300 y 500")
        else:
            print("Total entre 100 y 300")

#---------------------------------------
# Condicional de ingualdad son ==
#---------------------------------------
elif total == 100:
    print("Total es 100")
else:
    print("Total menor que 100")

#=============================================
# Contador mietras la condicion sea verdadera
#=============================================
num=0
while num<5:
    num = num + 1
    print("num = ", num)

num = 0
while num < 5:
    num +=1              #num +=1 es lo mismo que num = num + 1
    print("num = ", num)
    if num == 3:         # condicion antes de salir del bucle
        break

num=0
while num<5:
    num+=1
    if num > 3:
        continue # evita lo que sigue, continuar con las interaciones
    print("num = ", num)

#======================
# Bucle sobre lista
#======================
nums = [10,20,30,40,50]
for i in nums:
    print(i)

#=========================
# Bucle sobre un string
#=========================
for char in "Hello":
    print(char)

#=============================
# Bucle sobre un diccionario
# intems = elementos
#=============================
numNames = {1:"One", 2:"Two", 3: "Three"}
for pair in numNames.items():
    print(pair)

#=================================
# Bucle sobre diccionario
# key = llave
# value = valor
#=================================
for k,v in numNames.items():
    print("key = ", k, "value = ",v)

#++++++++++++++++++++++++++++++++++++++++++++
# FUNCIONES
#++++++++++++++++++++++++++++++++++++++++++++

#======================
# Primera funcion
#======================
def saludo():
    #------------------------------------
    # Documentacion rápida de la funcion
    #------------------------------------
     '''Esta función saluda'''
    print("¡Quiuboles con los chavos! libro de Yordi Rosado")

#========================
# Llamado de la funcion
#========================
saludo()

#==============================
# Se ejecuta pero no se asigna
#==============================
salida = saludo()

#===================
# Esto no funciona
#===================
print(salida)

#==========================
# Mostrar Documentacion
#==========================
#help(saludo)

#==========================
# Funcion con argumento
#==========================
def salud2(nombre):
    """"Esta funcion te saluda por tu nombre"""
    print("!Que onda ", nombre,"¡")
salud2("Jerson")
salud2("Sana")

#=================================
# Ahorrar trabajo del interprete
# nombre:str la varible es un str
#=================================
def saludos(nombre:str):
    """Esta funcion te saluda por tu nombre estrictamente"""
    print("!Que pasó ", nombre,"¡")
    
a=123
print(type(a))
saludos("Jerson")
saludos(a)

#=====================================
# Funcion con muchos argumentos
#=====================================
def saludos_multiples(nombre1, nombre2, nombre3):
    """Esta funcón salida a 3 personas la mismo tiempo"""
    print("Hola", nombre1, nombre2, "y", nombre3)
    
saludos_multiples("Jerson", "Marcus", "Eren")

#=============================================
# Función con cualquier número de argumentos
#=============================================
def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i=0
    #=================================
    # end= es para ponerlo de corrido
    #=================================
    print("Hola ", end="")
    while len(nombres)>i:
        # Ultimo nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            # Cualquier otro nombre
            print(nombres[i], end=", ")
        i+=1
        
muchos_saludos("Jerson", "Sana", "Tanjiro", "Eren")


#===========================================
# Función con argumentos escondidos **
#===========================================

def greet(**person):
    #=====================================================
    # persona tiene características firstname y lastname
    #=====================================================
    print("Hello", person["firstname"], person["lastname"])

#==============================================
# Llamar la función con argumentos en desorden
#==============================================
greet(lastname="Jobs", firstname="Steve") # Se pueden especificar las variables en desorden
greet(firstname="Calvin", lastname="Harris")
greet(lastname="Ronaldo", firstname="Cristiano")
greet(firstname="Bill", lastname="Gates", age=55) # se  pueden pasar mas pramentross de los necesarios

#=====================================
# Función con los valores por defecto
#=====================================
def greet(name="Guest"):
    print("Hello", name)

greet() # Utiliza el valor por defecto
greet("Cronos")

#=======================
# Función con resultado
#=======================
def suma(a,b):
    return a+b

#=========================
# Programación funcional 
#=========================
total=suma(4, suma(4,230))
print(total)
 
#==================================================
# Calculo lambda
# nombre de la función = lambda variable : función
#==================================================
x_al_cuadrado = lambda x: x*x
al = x_al_cuadrado(5)
print(al)

#===============================
# Lambda de varias variables
#===============================
suma = lambda x1,x2,x3 : x1+x2+x3
print(suma(32,5,364))

sumas = lambda *x: x[0] +x[1] + x[2] +x[3]
print(sumas(100,200,300,400))

#===========================================
# Uso de una función anónima 
# El argumento va afuera entre párentesis
#===========================================

print((lambda x: x*x)(6)) #función anónima

#==================================
# Función ocn variable global
# EVITE EL EXCESO!!!!!!
#==================================
name="Steve"
def greet():
    global name # Para utilizar una variable global (que viene de fuera del bloque)
    name="Hertzz"
    print("Hello", name)
    
greet()

