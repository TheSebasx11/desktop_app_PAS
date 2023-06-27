import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"registerhorarios.kv"))


class RegisterHorariosLayout(BoxLayout):
    def increase_number(self, number):
        print(f"Increasing number: {number}")

class RegisterHorarios(Screen):
     def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(RegisterHorariosLayout())


"""class RegisterHorarios(App):
    def build(self):
        return RegisterHorariosLayout()
"""
if __name__ == '__main__':
    RegisterHorarios().run()
