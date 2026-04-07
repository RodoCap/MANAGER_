import json 
import os
from cryptography.fernet import Fernet

class GestorModel:

    # Constructor

    # Inicializa las rutas de los archivos utilizados en el sistema
    def __init__(self):
        self.archivo_json = "passwords.json"
        self.archivo_cifrado = "datos.key"
        self.archivo_clave = "clave.key"


    # Genera la clave

    # Crea una clave simétrica si no existe previamente
    def generar_clave(self):
        if not os.path.exists(self.archivo_clave):
            clave = Fernet.generate_key()
            with open(self.archivo_clave, "wb") as f:
                f.write(clave)
            return "Clave generada"
        return "La clave ya existe"


    # Carga la clave

    # Lee la clave almacenada en el archivo de claves
    def cargar_clave(self):
        return open(self.archivo_clave, "rb").read()


    # Guardar contraseña
    # Almacena un servicio con usuario, contraseña y categoría en el archivo json
    def guardar_password(self, servicio, usuario, password, categoria):
        try:
            with open(self.archivo_json, "r") as f:
                datos = json.load(f)
        except:
            datos = {}

        datos[servicio] = {
            "usuario": usuario,
            "password": password,
            "categoria": categoria
        }

        with open(self.archivo_json, "w") as f:
            json.dump(datos, f, indent=4)

        return "Guardado correctamente"


    # Cifra los datos

    # Cifra el contenido del json y lo guarda en un archivo protegido
    def cifrar(self):
        if not os.path.exists(self.archivo_json):
            return "No existe JSON"

        clave = self.cargar_clave()
        fernet = Fernet(clave)

        with open(self.archivo_json, "rb") as f:
            datos = f.read()

        datos_cifrados = fernet.encrypt(datos)

        with open(self.archivo_cifrado, "wb") as f:
            f.write(datos_cifrados)

        os.remove(self.archivo_json)

        return "Datos cifrados"


    # Descifra los datos

    # Recupera el archivo cifrado y reconstruye el archivo json original
    def descifrar(self):
        if not os.path.exists(self.archivo_cifrado):
            return None, "No existe archivo cifrado"

        clave = self.cargar_clave()
        fernet = Fernet(clave)

        with open(self.archivo_cifrado, "rb") as f:
            datos_cifrados = f.read()

        try:
            datos = fernet.decrypt(datos_cifrados)

            with open(self.archivo_json, "wb") as f:
                f.write(datos)

            datos_json = json.loads(datos.decode())

            return datos_json, "Datos descifrados"

        except:
            return None, "Error al descifrar"


    # Elimina el servicio
    
    # Elimina un registro específico del archivo json
    def eliminar(self, servicio):
        if not os.path.exists(self.archivo_json):
            return "Debes descifrar primero"

        with open(self.archivo_json, "r") as f:
            datos = json.load(f)

        if servicio in datos:
            del datos[servicio]

            with open(self.archivo_json, "w") as f:
                json.dump(datos, f, indent=4)

            return "Eliminado"

        return "No existe"