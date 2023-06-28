from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class Empleado:
    def __init__(self, nombres, segundo_nom, primer_ape, segundo_ape, documento, telefono, email, usuario):
        self.nombres = nombres
        self.segundo_nom = segundo_nom
        self.primer_ape = primer_ape
        self.segundo_ape = segundo_ape
        self.documento = documento
        self.telefono = telefono
        self.email = email
        self.usuario = usuario


class FormularioUserView(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 10
        self.background_color = (1, 1, 1, 1)  # Fondo blanco
        
        # Etiqueta "Hotel Trivoli"
        lbl_hotel = Label(text='Hotel Trivoli', color=(1, 1, 1, 1), font_size=30, size_hint=(1, 0.3),
                          pos_hint={'top': 1})

        # Etiqueta "Registro de Empleados"
        lbl_registro = Label(text='Registro de Empleados', color=(1, 1, 1, 1), font_size=20,pos_hint={'center_x':0.5,'center_y':0.5})

        # Campo primer nombre
        lbl_nombres = Label(text='Primer Nombre:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=20,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_nombres = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})

        # Campo segundo nombre
        lbl_segundo_nom = Label(text='Segundo Nombre:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=20,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_segundo_nom = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})

        # Campo Primer Apellido
        lbl_primer_ape = Label(text='Primer Apellido:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=20,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_primer_ape = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})

        # Campo Segundo Apellido
        lbl_segundo_ape = Label(text='Segundo Apellido:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=20,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_segundo_ape = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})

        # Campo Documento de Identidad
        lbl_documento = Label(text='Documento de Identidad:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=20,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_documento = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})

        # Campo Telefono
        lbl_telefono = Label(text='Telefono:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=20,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_telefono = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})

        # Campo Email
        lbl_email = Label(text='Email:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=20,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_email = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})

        # Campo Usuario
        lbl_usuario = Label(text='Usuario:', color=(1, 1, 1, 1), size_hint=(0.3, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})
        self.txt_usuario = TextInput(multiline=False, size_hint=(0.5, None), height=30,pos_hint={'center_x':0.5,'center_y':0.5})

        # Contenedor para los botones
        btn_layout = BoxLayout(size_hint=(0.5, None), height=30, spacing=10,pos_hint={'center_x':0.5,'center_y':0.5})

        # Botón Registrar
        btn = Button(
            text='Registrar',
            background_color=(0.031, 0.129, 0.102, 1),  # Color de fondo del botón 1
            color=(1, 1, 1, 1),  # Color del texto en blanco
            size_hint=(0.3, None),  # Tamaño pequeño
            height=30,
            pos_hint={'center_x': 0.5}  # Centrado horizontalmente
        )
        btn.bind(on_release=self.registrar_empleado)

        # Agregar los botones al contenedor
        btn_layout.add_widget(btn)

        # Agregar los elementos al diseño
        self.add_widget(lbl_hotel)
        self.add_widget(lbl_registro)
        self.add_widget(lbl_nombres)
        self.add_widget(self.txt_nombres)
        self.add_widget(lbl_segundo_nom)
        self.add_widget(self.txt_segundo_nom)
        self.add_widget(lbl_primer_ape)
        self.add_widget(self.txt_primer_ape)
        self.add_widget(lbl_segundo_ape)
        self.add_widget(self.txt_segundo_ape)
        self.add_widget(lbl_documento)
        self.add_widget(self.txt_documento)
        self.add_widget(lbl_telefono)
        self.add_widget(self.txt_telefono)
        self.add_widget(lbl_email)
        self.add_widget(self.txt_email)
        self.add_widget(lbl_usuario)
        self.add_widget(self.txt_usuario)
        self.add_widget(btn_layout)

    def registrar_empleado(self, *args):
        nombres = self.txt_nombres.text
        segundo_nom = self.txt_segundo_nom.text
        primer_ape = self.txt_primer_ape.text
        segundo_ape = self.txt_segundo_ape.text
        documento = self.txt_documento.text
        telefono = self.txt_telefono.text
        email = self.txt_email.text
        usuario = self.txt_usuario.text

        empleado = Empleado(nombres, segundo_nom, primer_ape, segundo_ape, documento, telefono, email, usuario)

        # Realizar cualquier acción adicional con el objeto "empleado"
        # por ejemplo, almacenarlo en una base de datos, mostrarlo en la interfaz, etc.
        print(vars(empleado))

        # Reiniciar los campos de entrada
        self.txt_nombres.text = ''
        self.txt_segundo_nom.text = ''
        self.txt_primer_ape.text = ''
        self.txt_segundo_ape.text = ''
        self.txt_documento.text = ''
        self.txt_telefono.text = ''
        self.txt_email.text = ''
        self.txt_usuario.text = ''


class MyApp(App):
    def build(self):
        return FormularioUserView()


if __name__ == '__main__':
    MyApp().run()
