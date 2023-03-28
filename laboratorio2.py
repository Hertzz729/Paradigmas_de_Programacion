#=======================
# Conjunto en python
#=======================
even_num = {2,4,6,10} # conjunto de números pares
print(even_num)

# El bool no es parte del conjunto
emp = {1, 'Steve', 10.5, True}
print(emp)

nums = {1,2,2,3,4,4,5,5}
print(nums)

#===============================
# Convertir secuecia a conjunto
# No lo genera en orden
#===============================

s = set('Hello')
print(s)
s = set((1,2,3,4,5)) # tupla a conjunto
print(s)

#==============================================
# De diccionario a conjunto: conjunto de llaves
#==============================================

d = {1: 'One', 2: 'Two'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 # Unión
print(su)

si = s1&s2 # Intersección
print(s1)

sr = s1-s2 # Diferencia de conjuntos
print(sr)

sp = s2-s1
print(sp)

ss = s1^s2 # Diferencai simetrica
print(ss)

#===============================
# Uso de diccionarios
#===============================
capitals = {"USA":"Washington D.C.", "France": "Paris", "India":"Nueva Delhi"}
print(capitals)

#==================
# Llave:valor
#==================
# diccionario vacío
d = {}

# Llace entera, valor sting
numsNames={1:"One",2:"Two", 3:"Three"}

# Llave real, valor string
decNames = {1.4: "One and half", 2.5:"Two and half", 3.5:"Three and half"}

# Llave tupla, valot string
items={("Parker", "Reynolds", "Camlin"):"pen", ("LG", "Whirlpool", "Samsung"):"Refrigerator"}

#Llave string, valor int
romanNums = {"I":1, "II":2, "III":3, "IV":4, "V":5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("India"))

# Reportar llave y valor
for k in capitals:
    print("Key = " + k + "Value = " + capitals[k])

#Nuevo dato para el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar todo el diccionario
del capitals

# Reportar llaves 
print(romanNums.keys())

#Reportar valores
print(romanNums.values())

# Juicio de llave (está o no está la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)


#++++++++++++++++++++++++++++++++++++++++++++
# LISTAS 
# Las listas pueden ser de pbjetos diferentes
#++++++++++++++++++++++++++++++++++++++++++++
miprimeralista = [] #Lista vacía
print(miprimeralista)

#+++++++++++++++++++++++++
# Llenado de lista
#+++++++++++++++++++++++++
miprimeralista = [1,"Xavi", 1.34, "Ruleman", "Jerson", "Hertzz79", True]
print(miprimeralista)

#++++++++++++++++++++++++++++++++++++
# list: hacer una lista
# range(i,j): secuencia de i hata j.1
#++++++++++++++++++++++++++++++++++++
nums = list(range(1,61))

for i in nums:
    print(i)

#++++++++++++++++++++++++++++++++++++++
# Inlcuir nuevos elementos en la lista
#++++++++++++++++++++++++++++++++++++++
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#++++++++++++++++++++++++++++++++++++++
# Quitar elementos de la lista
#++++++++++++++++++++++++++++++++++++++
nums.remove(61)
print(nums)

#++++++++++++++++++++++++++++++++
# Quitar el elemento con idice i
#++++++++++++++++++++++++++++++++
i = 61
del nums[i]
print(nums)

#++++++++++++++++++++++++
# Borrar la lista
#++++++++++++++++++++++++
del nums

#++++++++++++++++++++++++
# Sumar listas
#++++++++++++++++++++++++
L1 = [1,2,3]
L2 = [4,5,6]
print(L1, L2)

#+++++++++++++++++++++++++++++++
# Llenado a mano
#+++++++++++++++++++++++++++++++
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial)

#+++++++++++++++++++++++++++++++++++
# Genera una tupla con la lista
#+++++++++++++++++++++++++++++++++++
potencial = tuple(potencial)
print(potencial)









