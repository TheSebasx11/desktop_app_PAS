import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
import os


currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"ventanaprincipal.kv"))



class PrincipalViewLayout(BoxLayout):
    pass

class Ventana_PrincipalScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(PrincipalViewLayout())

""" class Ventana_PrincipalScreen(App):
    def build(self):
        return MyLayout() """

if __name__ == '__main__':
    Ventana_PrincipalScreen().run()
