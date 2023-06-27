import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('ventanaprincipal.kv')



class MyLayout(BoxLayout):
    pass

class Ventana_Principal(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Ventana_Principal().run()
