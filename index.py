from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from views.Assist_View.assist_view import Assist_View
from views.registro_admin import FormularioAdminView
from views.Login_View.login_view import LoginView
from views.Landing_page.main_view import MainView_View
from views.Reports_view.report_view import ReportView
from views.Consultas_view.consultEmployee_view import ConsultView_View
from views.ConsultaSch_view.consultSch_view import ConsultSchView_View
from views.windowprin.ventana_principal import Ventana_PrincipalScreen
from views.Register_Sch_Empl.registro_empleado import FormularioUserView
from views.asignar_horarios.asignarhorarios import AsignarHorarios
from views.register_horario.registerhorario import RegisterHorarios

class MyApp(App):
    
   
    
    def build(self):
       
        sm = ScreenManager()
        #Create ur view
        ass_view = Assist_View(name = "assist_view")
        formAdmin = FormularioAdminView(name = "form_admin")
        log_view = LoginView(name = "login_view")
        admin_main_view = MainView_View(name = "admin_main_view")
        report_view = ReportView(name = "report_view")
        consultEmp_view = ConsultView_View(name="consultEmp_view")
        consultSch_view = ConsultSchView_View(name="consultSch_view")
        principal_view = Ventana_PrincipalScreen(name = "principal_view")
        formUser = FormularioUserView(name="form_user")
        assign_sch = AsignarHorarios(name="assign_sch")
        register_sch = RegisterHorarios(name = "register_sch")
        
        # Add ur view to the manager
        sm.add_widget(ass_view)
        sm.add_widget(formAdmin)
        sm.add_widget(log_view)
        sm.add_widget(admin_main_view)
        sm.add_widget(report_view)
        sm.add_widget(consultEmp_view)
        sm.add_widget(consultSch_view)
        sm.add_widget(principal_view)
        sm.add_widget(formUser)
        sm.add_widget(assign_sch)
        sm.add_widget(register_sch)
        

        #Put ur view name on the current and run

        sm.current = "login_view"   
            
        return sm
    

if __name__ == "__main__":
    MyApp().run()
