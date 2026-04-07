from model.gestor_model import GestorModel
from view.gui_view import GUIView
from controller.gestor_controller import GestorController

def main():
    model = GestorModel()
    view = GUIView()
    controller = GestorController(model, view)

    view.set_controller(controller)
    view.iniciar()

if __name__ == "__main__":
    main()