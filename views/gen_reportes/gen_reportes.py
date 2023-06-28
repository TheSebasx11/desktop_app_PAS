from kivy.app import App
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen
import requests

currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"genreportes.kv"))

class GenReportesLayout(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.generateTable()
    
    def generateTable(self):
        
        url_test = "https://frigosinu.andrea.com.co/lila/api/informe/puntuales"
        data = requests.get(url_test)
        data = data.json()
        cols = len(data[0])
        print(f"{len(data[0])}")
        table_layout = self.ids.table_layout
        
        table_layout.cols = cols
        
        print(f"Cols table: {table_layout.cols}")
        
        for row in data:
            print(f"{row}")
        
        pass


""" class GenReportesView(App):
    def build(self):
        return GenReportesLayout()
"""

class GenReportesView(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(GenReportesLayout())

"""     
if __name__ == '__main__':
    GenReportesView().run() """
