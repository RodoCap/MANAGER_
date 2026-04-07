import json
import os
from cryptography.fernet import Fernet

class GestorModel:

    
    # Configuracion inicial
    # Define las rutas de almacenamiento
    def __init__(self):
        self.ruta_json = "passwords.json"
        self.ruta_cifrado = "datos.key"
        self.ruta_clave = "clave.key"


    
    # Crear clave
  
    def generar_clave(self):
        if os.path.exists(self.ruta_clave):
            return "La clave ya fue creada anteriormente"

        nueva_clave = Fernet.generate_key()
        with open(self.ruta_clave, "wb") as archivo:
            archivo.write(nueva_clave)

        return "Clave creada correctamente"


    # =========================
    # OBTENER CLAVE
    # =========================
    def obtener_clave(self):
        with open(self.ruta_clave, "rb") as archivo:
            return archivo.read()


    # =========================
    # GUARDAR DATOS
    # =========================
    def guardar_password(self, servicio, usuario, password, categoria):

        if os.path.exists(self.ruta_json):
            try:
                with open(self.ruta_json, "r") as archivo:
                    info = json.load(archivo)
            except:
                info = {}
        else:
            info = {}

        info[servicio] = {
            "usuario": usuario,
            "password": password,
            "categoria": categoria
        }

        with open(self.ruta_json, "w") as archivo:
            json.dump(info, archivo, indent=4)

        return "Registro almacenado"


    # =========================
    # CIFRAR DATOS
    # =========================
    def cifrar(self):
        if not os.path.exists(self.ruta_json):
            return "No hay datos para proteger"

        clave = self.obtener_clave()
        encriptador = Fernet(clave)

        with open(self.ruta_json, "rb") as archivo:
            contenido = archivo.read()

        contenido_cifrado = encriptador.encrypt(contenido)

        with open(self.ruta_cifrado, "wb") as archivo:
            archivo.write(contenido_cifrado)

        os.remove(self.ruta_json)

        return "Información cifrada correctamente"


    # =========================
    # DESCIFRAR DATOS
    # =========================
    def descifrar(self):
        if not os.path.exists(self.ruta_cifrado):
            return None, "No se encontró archivo cifrado"

        clave = self.obtener_clave()
        encriptador = Fernet(clave)

        with open(self.ruta_cifrado, "rb") as archivo:
            contenido_cifrado = archivo.read()

        try:
            contenido = encriptador.decrypt(contenido_cifrado)

            with open(self.ruta_json, "wb") as archivo:
                archivo.write(contenido)

            datos = json.loads(contenido.decode())

            return datos, "Datos recuperados correctamente"

        except:
            return None, "No fue posible descifrar"


    # =========================
    # ELIMINAR DATOS
    # =========================
    def eliminar(self, servicio):
        if not os.path.exists(self.ruta_json):
            return "Primero debes recuperar los datos"

        with open(self.ruta_json, "r") as archivo:
            info = json.load(archivo)

        if servicio not in info:
            return "Servicio no encontrado"

        del info[servicio]

        with open(self.ruta_json, "w") as archivo:
            json.dump(info, archivo, indent=4)

        return "Registro eliminado"