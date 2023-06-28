from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
import os

currentFilePath = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(currentFilePath,"loginview.kv"))
#Builder.load_file('loginview.kv')

class MyLayout(Widget):
    
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_button_pressed(self, email, password):
        # Realizar la validación y lógica de inicio de sesión aquí
        # Puedes comparar el email y la contraseña con los valores predeterminados

        if email == "admin" and password == "pas2023":
            # Iniciar sesión exitosamente
            print("Inicio de sesión exitoso")
            login_view = self.parent  # Obtener la instancia del controlador LoginView
            login_view.manager.current = "admin_main_view"  # Cambiar a la otra vista definida en el archivo de configuración
        else:
            # Credenciales inválidas
            print("Credenciales inválidas")
        
    
        
class LoginView(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(MyLayout())

    """def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()"""
    
    
"""if __name__ == '__main__':
    LoginView().run()"""