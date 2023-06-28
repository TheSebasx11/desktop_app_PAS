from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.graphics import Color, Line
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from datetime import datetime
import os
import sys
import requests
import kivy.properties as props

currentFilePath = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(currentFilePath, "consultas_view.kv"))
sys.path.append(currentFilePath)


class ConsultSchViewLayout(Widget):
    search_input = None  # Referencia al TextInput
    row_data = []

    def __init__(self, **kw):
        super().__init__(**kw)
        self.generate_labels()

    def generate_labels(self):
        url = "https://frigosinu.andrea.com.co/lila/api/horarios/"
        response = requests.get(url)
        data = response.json()

        self.row_data = [
            ["id", "Hora inicio", "Hora final"],
        ]

        for item in data:
            self.row_data.append(
                [item["idhorarios"],
                 item["hora_inicio"],
                 item["hora_fin"]
                 ]
            )

        table_layout = self.ids.table_layout

        for row in self.row_data:
            for data in row:
                label = Label(text=str(data))
                table_layout.add_widget(label)

        for _ in range(len(self.row_data)):
            line = TableLine()
            table_layout.add_widget(line)

    def search(self):
        search_name = self.search_input.text
    
        if search_name:
            filtered_data = []
            for row in self.row_data:
                if isinstance(row[0], int) and int(search_name) == row[0]:
                    filtered_data.append(row)
    
            # Actualizar la tabla con los datos filtrados
            self.ids.table_layout.clear_widgets()
    
            # Agregar los registros filtrados al comienzo de la tabla
            for row in filtered_data[::-1]:
                for data in row:
                    label = Label(text=str(data))
                    self.ids.table_layout.add_widget(label)
    
            # Volver a agregar las líneas horizontales entre filas
            for _ in range(len(filtered_data)):
                line = TableLine()
                self.ids.table_layout.add_widget(line)
    
    


class ConsultSchView_View(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(ConsultSchViewLayout())


class TableLine(BoxLayout):
    def __init__(self, **kwargs):
        super(TableLine, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 1

        with self.canvas:
            Color(0.5, 0.5, 0)

       