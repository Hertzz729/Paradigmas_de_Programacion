from aplicacion.repositorio.reposiotoriodeususarios import RepositorioDeUsuarios
from aplicacion.modelos.usaurio import Usuario

#====================================================
# S3 es hijo de RepositorioDeUsuario
#====================================================
class S3(RepositorioDeUsuarios):
    __clientId: str
    __secretKey: str
    __bucket: str

    def __int__(mi,clientId:str, secretKey:str, bucket:str):
        mi.__clientId = clientId
        mi.__secretKey = secretKey
        mi.__bucket = bucket

    def arbrir(mi)-> None:
        print(f"Estableciendo conexion a AWS S3 {mi, clietID}:{mi.__secretKey}")

    def guardar(mi, usario:Usuario)->None:
        userData = {"nombre": usuario.getNombre(),
                     "apellido": usuario.getApellido(),
                     "edad":usario.getEdad()}
        print(f"Guardando usuario de la bandeja:{mi.__bucket}:{userData}")

    def cerrar(mi)->None:
        print("Cerrando conexion AWS S3")

