from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from views.assist_view import Assists_View




class MyApp(App):
    def build(self):
        scManager = ScreenManager()
        ass_view = Assists_View(name = "assist_view")

        scManager.add_widget(ass_view)

        scManager.current = "assist_view"

        return scManager
    


if __name__ == "__main__":
    MyApp().run()
