# URLApp.Main.py
import pandas as pd
import os
import sys
from kivy.app import App

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MainWindow(Screen):
    link1 = ObjectProperty(None)
    link2 = ObjectProperty(None)
    link3 = ObjectProperty(None)
    link4 = ObjectProperty(None)
    link5 = ObjectProperty(None)
    
    def submit(self):
        if (self.link1.text.count("economictrends.limequery") == 1 and self.link2.text.count("economictrends.limequery") == 1
        and self.link3.text.count("economictrends.limequery") == 1 and self.link4.text.count("economictrends.limequery") == 1
        and self.link5.text.count("economictrends.limequery") == 1):
            link1 = self.link1.text
            link2 = self.link2.text
            link3 = self.link3.text
            link4 = self.link4.text
            link5 = self.link5.text
            
            link_list = [[link1],[link2],[link3],[link4],[link5]]
            links = pd.DataFrame(link_list, columns=['links'])
            links.to_csv("LinksNoBorrar.csv")            
            MyMainApp.get_running_app().stop()
        else:
            InvalidForm()
         
class WindowManager(ScreenManager):
    pass            
            
def InvalidForm():
    
    pop = Popup(title='Información incorrecta',
                  content= Label(text='''
                        Porfavor revise los links ingresados\n
                            y vuelva a ingresarlo\n
                    Para continuar haga click afuera del recuadro'''),
                  size_hint=(None, None), size=(400, 400))   
    pop.open()
 
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)   
 
kv = Builder.load_file(resource_path("URLApp.KivyV01.kv")) #cargamos la estructura del app    
sm = WindowManager()


screens = [MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()