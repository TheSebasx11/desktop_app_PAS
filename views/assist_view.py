import kivy.uix.boxlayout
from kivy.uix.label import Label
import kivy.uix.anchorlayout
from kivy.uix.screenmanager import Screen

class Assists_View(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Label(text = "hola"))

        

