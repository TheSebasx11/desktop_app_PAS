from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.graphics import Color, Line
from kivy.uix.textinput import TextInput
import kivy.properties as props
import os
import requests

currentFilePath = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(currentFilePath, "consultas_view.kv"))


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

        # Tabla con 7 columnas
        self.table_layout = GridLayout(cols=3, spacing=5, size_hint_y=0.9)

        api_url = "https://frigosinu.andrea.com.co/lila/api/horarios/"
        response = requests.get(api_url)
        data = response.json()
        self.row_data = []
        for item in data:
            row = [
                str(item['idhorarios']),
                str(item['hora_inicio']),
                str(item['hora_fin']),
            ]
            self.row_data.append(row)

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
        search_text = self.search_input.text

        if search_text:
            filtered_data = []
            for row in self.row_data:
                if search_text.lower() in row[0].lower():  # Buscar por horarios o ID de horario
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


class TableApp(App):
    def build(self):
        return TableScreen()


if __name__ == '__main__':
    TableApp().run()
