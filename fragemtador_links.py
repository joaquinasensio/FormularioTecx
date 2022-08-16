import pandas as pd
import numpy as np
from openpyxl import load_workbook
import openpyxl
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
        canvas.before:
            Color:
                rgba:(0/255,51/255,102/255,1)
            Rectangle:
                pos:self.pos
                size:self.size
        
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
                root.archivos()
""")

class MainWindow(Screen):
    empresas10 = ObjectProperty(None)
    empresas5 = ObjectProperty(None)
    def archivos(self):
        emp10 = int(self.empresas10.text)
        emp5 = int(self.empresas5.text)

        links = pd.read_excel("Libro1.xlsx")
        links = links.links.sample(frac = 1).reset_index(drop=True) #orden aleatorio de links
        links = links.to_frame() 


        for i in range(0,emp10):
            links.iloc[0:10].to_excel('links - empresa '+str(i+1)+'.xlsx', index = False) 
            links = links.iloc[10: , :]
        
        with pd.ExcelWriter('Distribución de Formularios para empresas.xlsx', engine='xlsxwriter') as writer:
            for i in range(0,emp10):                    
                # Write each dataframe to a different worksheet.
                pd.read_excel('links - empresa '+str(i+1)+'.xlsx').to_excel(writer, sheet_name='links - empresa '+str(i+1), index = False) 

        for j in range(0,emp5):
            links.iloc[0:5].to_excel('links - empresa '+str(j+1+emp10)+'.xlsx')
            links = links.iloc[5: , :]

        links_empresas.get_running_app().stop()
        
class WindowManager(ScreenManager):
    pass

sm = WindowManager()
screens = [MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class links_empresas(App):
    def build(self):
        return sm

if __name__ == "__main__":
    links_empresas().run()