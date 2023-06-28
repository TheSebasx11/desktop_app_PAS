import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from datetime import datetime
from kivy.lang import Builder
from kivy.graphics import Color, Line
import requests

currentFilePath = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(currentFilePath,"main_view.kv"))


class MainViewLayout(Widget):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.generate_labels()
        
    def generate_labels(self):
        table_layout = self.ids.table_layout
        table_layout.clear_widgets()

        
        url = "https://frigosinu.andrea.com.co/lila/api/turnos/U"
        response = requests.get(url)
        data =  response.json()
        
        
        row_data = [
            ["Nombres", "Apellidos", "Entrada", "Salida"],
        ]

        for item in data:
            row_data.append(
                [item["name_01"],
                 item["lastname01"],
                 item["llegada"],
                 item["salida"],
                #str(datetime.strptime(item["llegada"], '%Y-%m-%dT%H:%M:%S.%fZ')) ,
                #str(datetime.strptime(item["salida"], '%Y-%m-%dT%H:%M:%S.%fZ')) , 
                ]
            )
        
        
        
       
        for row in row_data:
            for data in row:
                label = Label(text=f" {data}")
                table_layout.add_widget(label)
                
        for _ in range(len(row_data)):
            line = TableLine()
            table_layout.add_widget(line)
        

class MainView_View(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        self.add_widget(MainViewLayout())
        
    
        
class TableLine(BoxLayout):
    def __init__(self, **kwargs):
        super(TableLine, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 1

        with self.canvas:
            Color(0.5, 0.5, 0.5)
            self.line = Line(points=[0, 0, 0, 1], width=1)