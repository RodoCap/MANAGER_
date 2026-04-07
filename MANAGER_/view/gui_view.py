import tkinter as tk
from tkinter import messagebox

class GUIView:

    # Constructor interfaz
    # Inicializa la ventana principal y sus componentes
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestor de Contraseñas")
        self.root.geometry("400x500")

        # Inputs formulario
        # Campos para ingresar los datos del usuario
        tk.Label(self.root, text="Sitio").pack()
        self.entry_servicio = tk.Entry(self.root)
        self.entry_servicio.pack()

        tk.Label(self.root, text="Usuario").pack()
        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.pack()

        tk.Label(self.root, text="Contraseña").pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        tk.Label(self.root, text="Categoría").pack()
        self.entry_categoria = tk.Entry(self.root)
        self.entry_categoria.pack()

        # Botones acciones
        # Contenedor y botones para ejecutar funciones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        self.btn_generar = tk.Button(frame_botones, text="Generar Clave")
        self.btn_generar.grid(row=0, column=0, padx=5)

        self.btn_guardar = tk.Button(frame_botones, text="Guardar")
        self.btn_guardar.grid(row=0, column=1, padx=5)

        self.btn_cifrar = tk.Button(frame_botones, text="Cifrar")
        self.btn_cifrar.grid(row=0, column=2, padx=5)

        self.btn_descifrar = tk.Button(frame_botones, text="Descifrar")
        self.btn_descifrar.grid(row=0, column=3, padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar")
        self.btn_eliminar.grid(row=0, column=4, padx=5)

        # Area de texto
        # Muestra los datos recuperados al usuario
        self.texto = tk.Text(self.root, height=10)
        self.texto.pack()


    # Conectar controller
    # Asocia cada boton con su funcion en el controlador
    def set_controller(self, controller):
        self.btn_generar.config(command=controller.generar_clave)
        self.btn_guardar.config(command=controller.guardar)
        self.btn_cifrar.config(command=controller.cifrar)
        self.btn_descifrar.config(command=controller.descifrar)
        self.btn_eliminar.config(command=controller.eliminar)


    # Obtener datos
    # Recupera los valores ingresados en el formulario
    def obtener_datos(self):
        return (
            self.entry_servicio.get(),
            self.entry_usuario.get(),
            self.entry_password.get(),
            self.entry_categoria.get()
        )


    # Obtener servicio
    # Devuelve el servicio ingresado para operaciones especificas
    def obtener_servicio(self):
        return self.entry_servicio.get()


    # Mostrar mensaje
    # Muestra una alerta con informacion al usuario
    def mostrar_mensaje(self, msg):
        messagebox.showinfo("Info", msg)


    # Mostrar datos
    # Imprime los registros en el area de texto
    def mostrar_datos(self, datos):
        self.texto.delete("1.0", tk.END)
        for s, info in datos.items():
            self.texto.insert(
                tk.END,
                f"{s} | Usuario: {info['usuario']} | Password: {info['password']} | Categoria: {info['categoria']}\n"
            )


    # Limpiar campos
    # Borra el contenido de los inputs del formulario
    def limpiar_campos(self):
        self.entry_servicio.delete(0, tk.END)
        self.entry_usuario.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)


    # Iniciar aplicacion
    # Ejecuta el bucle principal de la interfaz grafica
    def iniciar(self):
        self.root.mainloop()