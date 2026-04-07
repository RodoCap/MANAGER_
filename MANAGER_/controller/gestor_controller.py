class GestorController:

    # Metodo constructor

    # Recibe el modelo y la vista para poder comunicarlos
    def __init__(self, model, view):
        self.model = model
        self.view = view


    # Generacion de clave

    # Solicita al modelo crear una clave y mostrar el resultado
    def generar_clave(self):
        msg = self.model.generar_clave()
        self.view.mostrar_mensaje(msg)


    # Guardar contraseña

    # Obtiene los datos desde la vista y los envía al modelo para guardarlos
    def guardar(self):
        servicio, usuario, password, categoria = self.view.obtener_datos()
        msg = self.model.guardar_password(servicio, usuario, password, categoria)
        self.view.mostrar_mensaje(msg)


    # Cifrar datos

    # Encarga al modelo cifrar la informacion almacenada
    def cifrar(self):
        msg = self.model.cifrar()
        self.view.mostrar_mensaje(msg)


    # Descifrar datos

    # Solicita al modelo recuperar la informacion y la muestra si existe
    def descifrar(self):
        datos, msg = self.model.descifrar()
        self.view.mostrar_mensaje(msg)

        if datos:
            self.view.mostrar_datos(datos)


    # Eliminar registro
    
    # Obtiene el servicio desde la vista y elimina el registro correspondiente
    def eliminar(self):
        servicio = self.view.obtener_servicio()
        msg = self.model.eliminar(servicio)
        self.view.mostrar_mensaje(msg)