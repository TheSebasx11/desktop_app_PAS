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
#from fingerprint_simpletest_rpi import get_fingerprint, finger, enroll_finger


currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"assist_view.kv"))

class AssistLayout(Widget):
    
    
       
    def __init__(self, **kw):
        super().__init__(**kw)
        button = self.ids.register_b
        button.bind(on_press=self.registerSch)
        
        
    def registerSch(self, *args):
        os.system("sudo python3 fingerprint_simpletest_rpi.py 1")
 
    
 #   def registerFinger(self, id):
 
    
    

class Assist_View(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(AssistLayout())
        
class Assist_View(App):
    def build(self):
        return AssistLayout()
        
if __name__ == '__main__':
    Assist_View().run()   
