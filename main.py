from npose import ClienteBancario

#================================================
# try: intenta (correr las intrucciones)
# except: atrapar el error en una variabel
# e se puede convertir a string 
#================================================

#================================================
# Error por sacar más dinero del que tiene 
#================================================

try: 
    cliente = ClienteBancario("Jaime Mausan", "Memin Pinguin", 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
#=============================================
# Excepcion es el objeto más general de error
#=============================================
except Exception as e:
    print("Error: "+ str(e))
    
#====================================
# Error por usar un atributo privado
#====================================
try:
    print(cliente.__nombres)
except Exception as ex:
    print("Error: " + str(ex))

#======================
# Forma correcta
#======================
print(cliente.nombres)
