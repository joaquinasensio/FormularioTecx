import pandas as pd
from kivy.app import App

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_string("""
<MainWindow>:
    name: "main"
    empresas10: empresas10
    empresas5: empresas5
 
    GridLayout:
        cols:1
        
        FloatLayout:
            size: root.width, root.height/2
            padding: 15
            
            Label:
                text: "Ingrese los valores que desee"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4
                                                   
            Label:
                text: "Empresas con 10 links"
                size_hint: 0.4,0.08
                pos_hint: {"x":0, "top":0.8-0.12}
                font_size: (root.width**2 + root.height**2) / 16**4                
            TextInput:
                id: empresas10
                pos_hint: {"x":0.5, "top":0.8-0.12}
                size_hint: 0.4, 0.12
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4
    
            Label:
                text: "Empresas con 5 links"
                size_hint: 0.4,0.08
                pos_hint: {"x":0, "top":0.8-0.12*2}                
                font_size: (root.width**2 + root.height**2) / 16**4
            TextInput:
                id: empresas5
                size_hint: 0.4, 0.12
                pos_hint: {"x":0.5, "top":0.8-0.12*2}                
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Continuar"
            font_size: (root.width**2 + root.height**2) / 14**4 
            on_release:            
                root.fechas()
                root.manager.transition.direction = "left"                 
                root.manager.current = 'Menu_Principal' 
""")