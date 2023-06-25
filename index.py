from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from views.Assist_View.assist_view import Assist_View
from views.registro_admin import FormularioView
from views.Login_View.login_view import LoginView
from views.Landing_page.main_view import MainView_View
from views.Reports_view.report_view import ReportView
from views.Consultas_view.consultEmployee_view import ConsultEmployeeScreen
from views.Consultas_view.consultSch_view import ConsultSchScreen



class MyApp(App):
    
   
    
    def build(self):
       
        sm = ScreenManager()
        #Create ur view
        ass_view = Assist_View(name = "assist_view")
        formUser = FormularioView(name = "form_user")
        log_view = LoginView(name = "login_view")
        main_view = MainView_View(name = "main_view")
        report_view = ReportView(name = "report_view")
        consultEmp_view = ConsultEmployeeScreen(name="consultEmp_view")
        consultSch_view = ConsultSchScreen(name="consultSch_view")

        # Add ur view to the manager
        sm.add_widget(ass_view)
        sm.add_widget(formUser)
        sm.add_widget(log_view)
        sm.add_widget(main_view)
        sm.add_widget(report_view)
        sm.add_widget(consultEmp_view)
        sm.add_widget(consultSch_view)
        

        #Put ur view name on the current and run

        sm.current = "main_view"   
            
        return sm
    

if __name__ == "__main__":
    MyApp().run()
