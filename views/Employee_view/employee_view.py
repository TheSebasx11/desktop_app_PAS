from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.button import Button
import os

Builder.load_file('employee_view.kv')


class TableLine(BoxLayout):
    def __init__(self, **kwargs):
        super(TableLine, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 1

        with self.canvas:
            Color(0.5, 0.5, 0.5)
            self.line = Line(points=[0, 0, 0, 1], width=1)


class TableScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(TableScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        # Contenedor principal con fondo verde
        container = BoxLayout(orientation='horizontal')

        # Contenedor principal para left_container1 y left_container2
        left_containers = BoxLayout(orientation='vertical', size_hint_x=0.2)  # Cambiar el tamaño del contenedor

       # Contenedor izquierdo 1 con color de fondo
        label_button_container = BoxLayout(orientation='horizontal', spacing=10, padding=(10, 0))
        label_container = BoxLayout(orientation='vertical', width='150dp', height=label_button_container.height, padding=(0, 0, 10, 0))
        label = Label(text='Gestion de empleados', halign='center', valign='middle', text_size=label_container.size)
        label_container.add_widget(label)
        button_small = Button(text='Small Button', size_hint=(None, None), size=('100dp', '40dp'))
        label_button_container.add_widget(label_container)
        label_button_container.add_widget(button_small)


        # Contenedor izquierdo 2 con color de fondo
        left_container2 = BoxLayout(orientation='vertical')
        button2 = Button(text='Botón 2', height=60)  # Cambiar el tamaño del botón
        left_container2.add_widget(button2)

        # Agregar los contenedores izquierdos al contenedor principal
        left_containers.add_widget(label_button_container)
        left_containers.add_widget(left_container2)

        # Agregar el contenedor de left_containers al contenedor principal
        container.add_widget(left_containers)

        # Tabla con 7 columnas
        table_layout = GridLayout(cols=7, spacing=5, size_hint_y=0.9, padding=[100, 0, 0, 0])
        table_layout.bind(minimum_height=table_layout.setter('height'))

        row_data = [
            ["Nombres", "Apellidos", "Identificacion", "Sexo", "Cargo", "Fecha nacimiento", "Email"],
            ["Dato1", "Dato2", "Dato3", "Dato4", "Dato5", "Dato6", "Dato7"],
            ["Dato1", "Dato2", "Dato3", "Dato4", "Dato5", "Dato6", "Dato7"],
            ["Dato1", "Dato2", "Dato3", "Dato4", "Dato5", "Dato6", "Dato7"],
            ["Dato1", "Dato2", "Dato3", "Dato4", "Dato5", "Dato6", "Dato7"],
            ["Dato1", "Dato2", "Dato3", "Dato4", "Dato5", "Dato6", "Dato7"],
            ["Dato1", "Dato2", "Dato3", "Dato4", "Dato5", "Dato6", "Dato7"],
        ]

        for row in row_data:
            for data in row:
                label = Label(text=data)
                table_layout.add_widget(label)

        # Agregar líneas horizontales entre filas
        for _ in range(len(row_data)):
            line = TableLine()
            table_layout.add_widget(line)

        # Agregar el table_layout al contenedor principal
        container.add_widget(table_layout)

        # Agregar el contenedor principal al TableScreen
        self.add_widget(container)


class TableApp(App):
    def build(self):
        return TableScreen()


if __name__ == '__main__':
    TableApp().run()
