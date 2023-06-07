from kivy.app import App
from kivy.uix.label import Label

class ExampleApp(App):
    def build(self):
        return Label(text="Hola, mundo!")

if __name__ == "__main__":
    ExampleApp().run()
