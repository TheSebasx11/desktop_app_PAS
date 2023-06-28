from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class EmpleadoAdmin:
    def __init__(self, nombres, apellidos, documento, email, usuario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento = documento
        self.email = email
        self.usuario = usuario


class FormularioAdminView(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 15
        self.background_color = (1, 1, 1, 1)  # Fondo blanco
        
        # Etiqueta "Hotel Trivoli"
        lbl_hotel = Label(text='Hotel Trivoli', color=(1, 1, 1, 1), font_size=30, size_hint=(1, 0.3),
                          pos_hint={'top': 1})
        
        # Etiqueta "Registro del Administrador"
        lbl_registro = Label(text='Registro de Administrador', color=(1, 1, 1, 1), font_size=20,pos_hint={'center_x':0.5,'center_y':0.5})
        
        # Campo Nombres
        lbl_nombres = Label(text='Nombres:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_nombres = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        
        # Campo Apellidos
        lbl_apellidos = Label(text='Apellidos:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_apellidos = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        
        # Campo Documento de Identidad
        lbl_documento = Label(text='Documento de Identidad:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_documento = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        
        # Campo Email
        lbl_email = Label(text='Email:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_email = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        
        # Campo Usuario
        lbl_usuario = Label(text='Usuario:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_usuario = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        
        # Contenedor para los botones
        btn_layout = BoxLayout(size_hint=(0.5, None), height=30, spacing=10,pos_hint={'center_x':0.5,'center_y':0.5})
        
        # Botón Volver
        btn = Button(
            text='Volver',
            background_color=(0.031, 0.129, 0.102, 1),  # Color de fondo del botón 1
            color=(1, 1, 1, 1),  # Color del texto en blanco
            size_hint=(0.5, None),  # Tamaño pequeño
            height=30,pos_hint={'center_x':0.5,'center_y':0.5}
        )
        
        # Botón Registrar   
        btn2 = Button(
            text='Registrar',
            background_color=(0.031, 0.129, 0.102, 1),  # Color de fondo del botón 2
            color=(1, 1, 1, 1),  # Color del texto en blanco
            size_hint=(0.5, None),  # Tamaño pequeño
            height=30,pos_hint={'center_x':0.5,'center_y':0.5}
        )
        
        # Agregar los botones al contenedor
        btn_layout.add_widget(btn)
        btn_layout.add_widget(btn2)
        
        # Agregar los elementos al diseño
        self.add_widget(lbl_hotel)
        self.add_widget(lbl_registro)
        self.add_widget(lbl_nombres)
        self.add_widget(self.txt_nombres)
        self.add_widget(lbl_apellidos)
        self.add_widget(self.txt_apellidos)
        self.add_widget(lbl_documento)
        self.add_widget(self.txt_documento)
        self.add_widget(lbl_email)
        self.add_widget(self.txt_email)
        self.add_widget(lbl_usuario)
        self.add_widget(self.txt_usuario)
        self.add_widget(btn_layout)
        
        # Registrar el evento de clic del botón Registrar
        btn2.bind(on_release=self.registrar)
        
    def registrar(self, instance):
        # Obtener los valores de los inputs
        nombres = self.txt_nombres.text
        apellidos = self.txt_apellidos.text
        documento = self.txt_documento.text
        email = self.txt_email.text
        usuario = self.txt_usuario.text
        
        # Crear un objeto EmpleadoAdmin con los datos ingresados
        empleados_admin = EmpleadoAdmin(nombres, apellidos, documento, email, usuario)
        
        # Imprimir el objeto empleados_admin en la consola
        print(empleados_admin.__dict__)


class MyApp(App):
    def build(self):
        return FormularioAdminView()


if __name__ == '__main__':
    MyApp().run()
