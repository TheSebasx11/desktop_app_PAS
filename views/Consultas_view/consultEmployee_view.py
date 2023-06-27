from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.graphics import Color, Line
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
import os
import sys
import requests
import kivy.properties as props

currentFilePath = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(currentFilePath, "consultas_view.kv"))
sys.path.append(currentFilePath)

class TableLine(BoxLayout):
    def __init__(self, **kwargs):
        super(TableLine, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 1
        self.search_input = TextInput()

        with self.canvas:
            Color(0.5, 0.5, 0.5)
            self.line = Line(points=[0, 0, 0, 1], width=1)


class TableScreen(BoxLayout):
    search_input = props.ObjectProperty()
    table_layout = props.ObjectProperty()
    row_data = []

    def __init__(self, **kwargs):
        super(TableScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        # Contenedor principal con fondo verde
        container = BoxLayout(orientation='vertical')
        container.size_hint_y = 0.9
        container.padding = [10, 10, 10, 10]
        container.spacing = 10

        self.table_layout = GridLayout(cols=7, spacing=5, size_hint_y=0.9)
        
        # Tabla con 7 columnas
        api_url = "https://frigosinu.andrea.com.co/lila/api/usuario/all"
        response = requests.get(api_url)
        data = response.json()
        self.row_data = []
        for item in data:
            row = [
                str(item['name_01']),
                str(item['lastname01']),
                str(item['identificacion']),
                str(item['sexo']),
                str(item['cargo']),
                str(item['fecha_nac']),
                str(item['email'])
            ]
            self.row_data.append(row)

        # Crear la tabla con los datos obtenidos de la API
        for row in self.row_data:
            for data in row:
                label = Label(text=data)
                self.table_layout.add_widget(label)

        # Agregar líneas horizontales entre filas
        for _ in range(len(self.row_data)):
            line = TableLine()
            self.table_layout.add_widget(line)

        container.add_widget(self.table_layout)
        self.add_widget(container)

    def search(self):
        search_name = self.search_input.text

        if search_name:
            filtered_data = []
            for row in self.row_data:
                if search_name.lower() in row[0].lower() or search_name.lower() in row[1].lower:  # Buscar en la primera columna (nombre)
                    filtered_data.append(row)

            # Actualizar la tabla con los datos filtrados
            self.table_layout.clear_widgets()
            for row in filtered_data:
                for data in row:
                    label = Label(text=data)
                    self.table_layout.add_widget(label)

            # Volver a agregar las líneas horizontales entre filas
            for _ in range(len(filtered_data)):
                line = TableLine()
                self.table_layout.add_widget(line)

class ConsultEmployeeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(TableScreen())

class TableApp(App):
    def build(self):
        return TableScreen()


if __name__ == '__main__':
    TableApp().run()
