import tkinter as tk
from tkinter import messagebox

class GUIView:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Administrador de Credenciales")
        self.ventana.geometry("400x500")

        tk.Label(self.ventana, text="Servicio").pack()
        self.input_servicio = tk.Entry(self.ventana)
        self.input_servicio.pack()

        tk.Label(self.ventana, text="Usuario").pack()
        self.input_usuario = tk.Entry(self.ventana)
        self.input_usuario.pack()

        tk.Label(self.ventana, text="Clave").pack()
        self.input_clave = tk.Entry(self.ventana, show="*")
        self.input_clave.pack()

        tk.Label(self.ventana, text="Categoria").pack()
        self.input_categoria = tk.Entry(self.ventana)
        self.input_categoria.pack()

        contenedor_botones = tk.Frame(self.ventana)
        contenedor_botones.pack(pady=10)

        self.boton_clave = tk.Button(contenedor_botones, text="Crear clave")
        self.boton_clave.grid(row=0, column=0, padx=5)

        self.boton_guardar = tk.Button(contenedor_botones, text="Registrar")
        self.boton_guardar.grid(row=0, column=1, padx=5)

        self.boton_cifrar = tk.Button(contenedor_botones, text="Proteger")
        self.boton_cifrar.grid(row=0, column=2, padx=5)

        self.boton_descifrar = tk.Button(contenedor_botones, text="Recuperar")
        self.boton_descifrar.grid(row=0, column=3, padx=5)

        self.boton_eliminar = tk.Button(contenedor_botones, text="Borrar")
        self.boton_eliminar.grid(row=0, column=4, padx=5)

        self.area_texto = tk.Text(self.ventana, height=10)
        self.area_texto.pack()

    # 🔴 AQUÍ ESTABA EL ERROR CORREGIDO
    def set_controller(self, controlador):
        self.boton_clave.config(command=controlador.crear_clave)  # antes: generar_clave ❌
        self.boton_guardar.config(command=controlador.registrar)
        self.boton_cifrar.config(command=controlador.proteger_datos)
        self.boton_descifrar.config(command=controlador.recuperar_datos)
        self.boton_eliminar.config(command=controlador.borrar)

    def obtener_datos(self):
        return (
            self.input_servicio.get(),
            self.input_usuario.get(),
            self.input_clave.get(),
            self.input_categoria.get()
        )

    def obtener_servicio(self):
        return self.input_servicio.get()

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Sistema", mensaje)

    def mostrar_datos(self, datos):
        self.area_texto.delete("1.0", tk.END)

        for servicio, info in datos.items():
            linea = f"{servicio} | Usuario: {info['usuario']} | Password: {info['password']} | Categoria: {info['categoria']}\n"
            self.area_texto.insert(tk.END, linea)

    def limpiar_campos(self):
        self.input_servicio.delete(0, tk.END)
        self.input_usuario.delete(0, tk.END)
        self.input_clave.delete(0, tk.END)
        self.input_categoria.delete(0, tk.END)

    def iniciar(self):
        self.ventana.mainloop()