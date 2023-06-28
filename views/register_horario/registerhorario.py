import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath, "registerhorarios.kv"))


class RegisterHorariosLayout(BoxLayout):
    def registrar_horario(self):
        hora_llegada = self.ids.hora_llegada_spinner.text
        minutos_llegada = self.ids.minutos_llegada_spinner.text
        hora_salida = self.ids.hora_salida_spinner.text
        minutos_salida = self.ids.minutos_salida_spinner.text

        horario_string = f'Horario de llegada: {hora_llegada}:{minutos_llegada}\nHorario de salida: {hora_salida}:{minutos_salida}'
        print(horario_string)  # Aquí puedes hacer lo que necesites con el string de horario


class RegisterHorarios(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(RegisterHorariosLayout())


""" class MyApp(App):
    def build(self):
        return RegisterHorarios() """



