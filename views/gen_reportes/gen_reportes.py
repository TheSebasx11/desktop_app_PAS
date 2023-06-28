from kivy.app import App
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
import requests

currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"genreportes.kv"))

class GenReportesLayout(BoxLayout):
    
    url = StringProperty()
    
    
    def __init__(self, **kw):
        super().__init__(**kw)
        
    
    
        
    
    def generateTable(self):
        
        text =  self.ids.report_spinner.text
        table_layout = self.ids.table_layout
        table_layout.clear_widgets()
        
        url = self.getUrlByText(text)
        
        """ data = requests.get()
        data = data.json() """
            
        data = requests.get(url)
        data = data.json()
        headers = list(self.getJSONTable(text,  data[0]).keys())
        table_layout.cols=len(headers)
        row_data = [
            headers
        ]
        
        for item in data:
            row_data.append(
                list(self.getJSONTable(text, item ).values())
            )
        
        """ for item in data:
            row_data.append(list(item.values())) """
        
        #print(f"Cols table: {row_data}")
               
        for row in row_data:
            for data in row:
                label = Label(text=f"{data}")
                table_layout.add_widget(label)
               
        #print(f"table {table_layout}")
        
        """ for row in data:
            for item in row:
                print(f"{item}") """
        
        
    def getUrlByText(self, text):
        if text == "Asistencia":
            return "https://frigosinu.andrea.com.co/lila/api/informe/numAsistencia"
        elif text == "Mas Faltantes":
            return "https://frigosinu.andrea.com.co/lila/api/informe/numInasistencia"
        elif text == "Mas puntuales": 
            return "https://frigosinu.andrea.com.co/lila/api/informe/puntuales"
    
    def getJSONTable(self, text, data):
        
        if text == "Asistencia":
            
            return {
                "Cantidad de Asistencias": data["Asistencia"],
                "Identificacion": data["identificacion"],
                "Primer nombre": data["name_01"],
                "Segundo nombre": data["name_02"],
                "Primer apellido": data["lastname01"],
                "Segundo apellido": data["lastname02"],
                "Nacimiento": data["fecha_nac"],
                "Genero": data["sexo"],
                "Email": data["email"],
                "Telefono": data["telefono"],
            }
        elif text == "Mas Faltantes":
            
            return {
                "Inasistencia": data["Inasistencia"],
                "Identificacion": data["identificacion"],
                "Primer nombre": data["name_01"],
                "Segundo nombre": data["name_02"],
                "Primer apellido": data["lastname01"],
                "Segundo apellido": data["lastname02"],
                "Nacimiento": data["fecha_nac"],
                "Genero": data["sexo"],
                "Email": data["email"],
                "Telefono": data["telefono"],
            }
        elif text == "Mas puntuales": 
            
            #        "Hora de inicio":
            #formatHour(DateTime.parse("2021-10-10T$horaInicio.000Z")),
            #"Edad": getAge(fechaNac),
            #"Llegada": formatHour(llegada),
            return {
                "Identificacion": data["identificacion"],   
                "Primer nombre": data["name_01"],
                "Segundo nombre": data["name_02"],
                "Primer apellido": data["lastname01"],
                "Segundo apellido": data["lastname02"],
                "Nacimiento": data["fecha_nac"],
                "Genero": data["sexo"],
                "Email": data["email"],
                "Telefono": data["telefono"],
            }
        
    
    def on_change_text(self, text):
        print(text)
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
