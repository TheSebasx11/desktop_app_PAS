from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from views.assist_view import Assists_View
from views.registro_admin import FormularioView
from views.Loginview.login_view import LoginView



class MyApp(App):
    def build(self):
        scManager = ScreenManager()

        #Create ur view
        ass_view = Assists_View(name = "assist_view")
        formUser = FormularioView(name = "form_user")

        log_view = LoginView(name = "login_view")

        # Add ur view to the manager
        scManager.add_widget(ass_view)
        scManager.add_widget(formUser)
        scManager.add_widget(log_view)

        #Put ur view name on the current and run

        scManager.current = "login_view"      

        return scManager
    


if __name__ == "__main__":
    MyApp().run()
