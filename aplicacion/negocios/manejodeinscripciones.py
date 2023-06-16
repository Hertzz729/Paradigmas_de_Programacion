from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorios.reposiotoriodeusuarios import RepositorioDeUsuarios

#================================
# Clase storemanager
# NO TIENE VARIABLES!!
#================================
class ManejoDeInscripciones:
    #================================================================
    # Decorador staticmethod
    # El onjeto solo tiene la funcion inscribirUsuario
    # ENVUEVEL LA FUNCION SIN LLAMAR VAIRABLES LOCALES
    # el onjeto ManejoDeInscripciones es la interface intercambiable
    #================================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios)->None:
        print("------->Guardando usuario...\n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()

