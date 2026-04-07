from model.gestor_model import GestorModel
from view.gui_view import GUIView
from controller.gestor_controller import GestorController

# Funcion principal

# Inicializa el modelo, la vista y el controlador, y los conecta entre si
def main():
    model = GestorModel()
    view = GUIView()
    controller = GestorController(model, view)

    # Asigna el controlador a la vista para permitir la comunicacion
    view.set_controller(controller)

    # Inicia la interfaz grafica de la aplicacion
    view.iniciar()

# Punto de entrada del programa

# Ejecuta la funcion principal cuando el archivo se ejecuta directamente
if __name__ == "__main__":
    main()