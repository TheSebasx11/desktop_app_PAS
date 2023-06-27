from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner


class MyLayout(BoxLayout):
    def increase_number(self, number):
        print(f"Increasing number: {number}")


class RegisterHorarios(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    RegisterHorarios().run()
