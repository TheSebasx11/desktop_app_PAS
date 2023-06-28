import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"asignarhorarios.kv"))


class AsignarHorariosLayout(BoxLayout, Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        print(f"root {self.children }")
        
        self.fill_data()
    
    def fill_data(self, *args):
        
        url_users = "https://frigosinu.andrea.com.co/lila/api/usuario/all"
        url_sch = "https://frigosinu.andrea.com.co/lila/api/horarios"
        response1 = requests.get(url_users)
        response2 = requests.get(url_sch)
        data1 =  response1.json()
        data2 =  response2.json()
        users = []
        schedules = []
        
        for item in data1:
            users.append(f"{item['idusuarios']} {item['name_01']} {item['lastname01']}")
            #print(f"{item['name_01']} {item['lastname01']}")
        for item in data2:
            schedules.append(f"{item['idhorarios']} {item['hora_inicio']} - {item['hora_fin']}")
        emp_spinner = self.ids.ass_emp_spinner
        sch_spinner = self.ids.ass_sch_spinner
        
        emp_spinner.values = users
        sch_spinner.values = schedules
        
        
    def sendData(self):
        emp_spinner = self.ids.ass_emp_spinner
        sch_spinner = self.ids.ass_sch_spinner
        user_id = emp_spinner.text[:1] 
        sch_id = sch_spinner.text[:1]
        url = f"https://frigosinu.andrea.com.co/lila/api/usuariohorario/updateHorario/{user_id}"
        print(f"{user_id} - {sch_id}")
        jsonObj = {
            "idhorario": sch_id
        }
        response =  requests.post(url, json=jsonObj, headers= {
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        
        print(f"response {response.status_code == 200}")
        
        
        
        if response.status_code == 200:
            print(f"{self.parent.parent}")
            #self.parent.current = "principal_view"
        
        
        

class AsignarHorarios(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        self.add_widget(AsignarHorariosLayout())

""" class AsignarHorarios(App):
    def build(self):
        return AsignarHorariosLayout()
 """

if __name__ == '__main__':
    AsignarHorarios().run()
