

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
kv = Builder.load_file(os.path.join(currentFilePath,"as_hue.kv"))


class AsignarHuellaLayout(BoxLayout, Screen):
    msg = ""
    
    def __init__(self, **kw):
        super().__init__(**kw)
        print(f"root {self.children }")
        
        self.fill_data()
    
    def fill_data(self, *args):
        
        url_users = "https://frigosinu.andrea.com.co/lila/api/usuario/all"
        
        response1 = requests.get(url_users)
        
        data1 =  response1.json()
    
        users = []
        
        
        for item in data1:
            users.append(f"{item['idusuarios']} {item['name_01']} {item['lastname01']}")
            #print(f"{item['name_01']} {item['lastname01']}")
        
        emp_spinner = self.ids.ass_emp_spinner
        
        
        emp_spinner.values = users
        
        
        
    def sendData(self):
        
        emp_spinner = self.ids.ass_emp_spinner
        
        user_id = emp_spinner.text[:2] 
        
        url = f"http://192.168.20.24:3000/api/huellas/{user_id}"
        os.system(f"sudo python3 fingerprint_simpletest_rpi.py {user_id}")
        print(f"{user_id} ")
        
        response =  requests.post(url, headers= {
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        
        print(f"response {response.status_code == 200}")
        if response.status_code == 200:
            self.msg = "Huella asignada para el usuario"
            self.ids.l_msg.text = self.msg
        
        
       
            #self.parent.current = "principal_view"
        
        
        

class AsignarHuella(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        self.add_widget(AsignarHuellaLayout())

class AsignarHuella(App):
    def build(self):
        return AsignarHuellaLayout()


if __name__ == '__main__':
    AsignarHuella().run()