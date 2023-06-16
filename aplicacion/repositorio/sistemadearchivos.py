from aplicacion.repositorio.repositoriodeususario import RepositorioDeUsuario
from aplicacion.modelos.usuario import Usuario

#=============================================
# Implementa la interface RepositorioDeUsuario
#=============================================
class SistemaDeArchivos(RepositorioDeUsuario):
    __directiorio: str

    def __int__(mi,directorio:str):
        mi.__directorio = directorio

    def abrir(mi)->None:
        print(f"Abrir directorio: {mi.__directorio}")

    def guardar(mi, usuario:Usuario)->None:
        xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
        print(f"Guardando usuario en el archivo : {mi.__directorio}/{usuario.getNombre()}")
        print(xml)

        def cerrar(mi)->None:
            print("Cerrando el archivo")

