from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.graphics import Color, Line
import os

currentFilePath = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(currentFilePath, "consultas_view.kv"))


class TableLine(BoxLayout):
    def __init__(self, **kwargs):
        super(TableLine, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 1

        with self.canvas:
            Color(0.5, 0.5, 0.5)
            self.line = Line(points=[0, 0, 0, 1], width=1)


class TableScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(TableScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        # Contenedor principal con fondo verde
        container = BoxLayout(orientation='vertical')
        container.size_hint_y = 0.9
        container.padding = [10, 10, 10, 10]
        container.spacing = 10

        # Tabla con 7 columnas
        table_layout = GridLayout(cols=7, spacing=5, size_hint_y=0.9)
        row_data = [
            ["ID", "Hora llegada", "Hora salida"],
            ["Dato1", "Dato2", "Dato3"],
            ["Dato1", "Dato2", "Dato3"],
            ["Dato1", "Dato2", "Dato3"],
            ["Dato1", "Dato2", "Dato3"],
            ["Dato1", "Dato2", "Dato3"],
            ["Dato1", "Dato2", "Dato3"],
        ]

        for row in row_data:
            for data in row:
                label = Label(text=data)
                table_layout.add_widget(label)

        # Agregar líneas horizontales entre filas
        for _ in range(len(row_data)):
            line = TableLine()
            table_layout.add_widget(line)

        container.add_widget(table_layout)
        self.add_widget(container)


class TableApp(App):
    def build(self):
        return TableScreen()


if __name__ == '__main__':
    TableApp().run()
