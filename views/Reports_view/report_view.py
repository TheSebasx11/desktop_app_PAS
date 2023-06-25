import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from datetime import datetime
from kivy.lang import Builder
from kivy.graphics import Color, Line
import requests

currentFilePath = os.path.dirname(os.path.abspath(__file__))
kv = Builder.load_file(os.path.join(currentFilePath,"report_view.kv"))

class ReportViewlayout(Widget):
    pass

class ReportView(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(ReportViewlayout())