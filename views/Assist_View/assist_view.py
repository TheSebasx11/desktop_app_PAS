import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"assist_view.kv"))

class AssistLayout(Widget):
    si = "si"
    
    

class Assist_View(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(AssistLayout())
        """ 
        anchor_lay = AnchorLayout(anchor_x = "center", anchor_y="center", padding = (10,10,10,10))
        boxM = BoxLayout(orientation = "vertical")
        box1 = BoxLayout(orientation = "horizontal", padding = (50,10), size_hint = (1,.3))
        box2 = BoxLayout(orientation = "horizontal", padding = (50,10))
        box3 = BoxLayout(orientation = "horizontal")
        anchor_lay.add_widget(boxM)
        boxM.add_widget(box1)
        boxM.add_widget(box2)
        boxM.add_widget(box3)

        anchor_lay.background_color = (255, 255 , 255 ,1)


        box1.add_widget(Label(text = "Hotel Trivoli", size_hint = (.9,.2)))

        #box2.add_widget(Label(text = "", size_hint=(.2,.2)))
        box2.add_widget(Button(text = "Comenzar Lectura", size_hint =(.9, .2)))
        box2.add_widget(Label(text = "", size_hint=(.2,.2)))
        box2.add_widget(Button(text = "Registrar Turno",  size_hint =(.9, .2)))
        #box2.add_widget(Label(text = "", size_hint=(.2,.2)))

        
        boxMini1 = BoxLayout(orientation = "vertical")
        boxMini1.add_widget(Label(text = "Huella Empleado"))
        boxMini1.add_widget(Label(text = "image1"))

        boxMini2 = BoxLayout(orientation = "vertical")
        boxMini2.add_widget(Label(text = "Foto Empleado"))
        boxMini2.add_widget(Label(text = "image2"))

        box3.add_widget(boxMini1)
        box3.add_widget(boxMini2)

        self.add_widget(anchor_lay)"""
        
   

