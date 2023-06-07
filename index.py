from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from views.assist_view import Assists_View




class MyApp(App):
    def build(self):
        scManager = ScreenManager()

        #Create ur view
        ass_view = Assists_View(name = "assist_view")


        # Add ur view to the manager
        scManager.add_widget(ass_view)

        #Put ur view name on the current and run

        scManager.current = "assist_view"

        return scManager
    


if __name__ == "__main__":
    MyApp().run()
