import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import requests
import subprocess
import tempfile
from picamera import PiCamera
import time
#from fingerprint_simpletest_rpi import get_fingerprint, finger, enroll_finger


currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"assist_view.kv"))

class AssistLayout(Widget):
    
    msg = "Esperando lectura"
       
    def __init__(self, **kw):
        super().__init__(**kw)
        #button = self.ids.register_b
        #button.bind(on_press=self.registerSch)
        
        
    def registerSch(self):
        #os.system("sudo python3 fingerprint_simpletest_rpi.py 1")
        
        cmd = "sudo python3 fingerprint_simpletest_rpi.py 1"
        output = ""
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen(cmd, stdout=tempf,shell=True)
            proc.wait()
            tempf.seek(0)
            output = tempf.read()    
            print(output)
        output = str(output.decode('utf-8', errors='replace'))
        output = output.strip()[-1:]
        print(f"{output.strip()[-1:]}")
        if output != "o":
            url = f"http://192.168.1.106:3000/api/turnos/{output}"
            camera = PiCamera()
            timestr = time.strftime("%Y%m%d_%H%M%S")
            image_path = "IMG_{}.png".format(timestr)
            camera.capture(image_path)
            camera.close()
            print("Captured image:", image_path)
            
            with open(image_path, 'rb') as archivo:
        # Enviar la solicitud HTTP POST con el archivo adjunto
                respuesta = requests.post(url, files={'imagen': archivo})
            print(f"{respuesta}")
            
            self.msg= f"Turno creado para el usuario #{output}"
            
        else:
            self.msg= f"No se reconoció la huella"
        self.ids.l_msg.text = self.msg
    
 #   def registerFinger(self, id):
 
    
    

class Assist_View(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(AssistLayout())
        
""" class Assist_View(App):
    def build(self):
        return AssistLayout()
        
if __name__ == '__main__':
    Assist_View().run()    """
