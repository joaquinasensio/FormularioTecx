# main.py
import pandas as pd
from kivy.app import App

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

#importamos archivo con funciones de web scraping
from Bases import *
import os # para borrar archivos
    
#lista para chequear que se ingresen valores númericos en los inputs de la app
x = range(9999)
y = []
for n in x:
    y.append(str(n))


class MainWindow(Screen):
    def fin(self):
        p1 = pd.read_csv('perfil1.csv') #respuestas a la primera pregunta
        p2 = pd.read_csv('perfil2.csv') #respuestas a la segunda pregunta
        p3 = pd.read_csv('perfil3.csv') #respuestas a la segunda pregunta
        p4 = pd.read_csv('perfil4.csv') #respuestas a la segunda pregunta
        p5 = pd.read_csv('perfil5.csv') #respuestas a la segunda pregunta
        urls = pd.read_csv('LinksNoBorrar.csv')
        urls = urls.links.sample(frac = 1).reset_index(drop=True) #orden aleatorio de links
        urls = urls.to_frame() 
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_window_position(-10000,0) # escondemos el web driver
        
        #loopeamos por la cantidad de respuestas en el df
        for user_id in range(len(urls)):
            driver.get(urls.links[user_id])
            driver = answers(driver = driver, df = p1, perfil_class = perfil1_clase, rta1 = rta1, rta2 = rta2, user_id = user_id)
            driver = answers2(driver = driver, df = p2, perfil_class = perfil2_clase, rta2a = rta2_a, rta2b = rta2_b,
                          rta2c = rta2_c, rta2d = rta2_d, rta2e = rta2_e, user_id = user_id)
            driver = answers3(driver = driver, df = p3, perfil3_class = perfil3_clase, rta3a = rta3_a, rta3b = rta3_b, user_id = user_id)
            driver = answers4(driver = driver, df = p4, perfil4_class = perfil4_clase, rta4a = rta4_a, rta4b = rta4_b, rta4c = rta4_c, user_id = user_id)
            driver = answers5(driver = driver, df = p5, perfil5_class = perfil5_clase, rta5a = rta5_a, rta5b = rta5_b, rta5c = rta5_c, user_id = user_id)
            driver = submit(driver = driver, element_class = submit_class)            
        
        driver.close() # cerramos el web driver
        os.remove("perfil1.csv") #borramos los archivos de la carpeta del usuario
        os.remove("perfil2.csv") #borramos los archivos de la carpeta del usuario
        os.remove("perfil3.csv") #borramos los archivos de la carpeta del usuario
        os.remove("perfil4.csv") #borramos los archivos de la carpeta del usuario
        os.remove("perfil5.csv") #borramos los archivos de la carpeta del usuario
        MyMainApp.get_running_app().stop()
        #Window.close()

class Perfil1(Screen):
    pm_actual = ObjectProperty(None)
    sdm_actual = ObjectProperty(None)
    
    pm_prev = ObjectProperty(None)
    sdm_prev = ObjectProperty(None)


    def submit(self):
        if ((self.pm_actual.text in y or self.pm_actual.text.count("") == 1) and (self.pm_prev.text in y or self.pm_prev.text.count("") == 1)
                and (self.sdm_actual.text in y or self.sdm_actual.text.count("") == 1) and (self.sdm_prev.text in y or self.sdm_prev.text.count("") == 1)):
            x1_11 = fragmentar(self.pm_actual.text)
            x1_12 = fragmentar(self.sdm_actual.text)
            
            x1_21 = fragmentar(self.pm_prev.text)
            x1_22 = fragmentar(self.sdm_prev.text)
            sm.current = "main"        
          
            perfil1_dict = {'x1_11':x1_11, 'x1_12':x1_12, 'x1_21':x1_21, 'x1_22':x1_22}
            df_perfil1 = pd.DataFrame.from_dict(perfil1_dict)
            df_perfil1.to_csv("perfil1.csv")
            
            self.reset() 
        else:
            invalidForm()
            sm.current = "perfil1"

        
    def reset(self):
        self.pm_actual.text = ""
        self.sdm_actual.text = ""
        
        self.pm_prev.text = ""
        self.sdm_prev.text = ""

class Perfil2(Screen):
    app_cs_actual = ObjectProperty(None)
    desar_web_actual = ObjectProperty(None)
    desar_juegos_actual = ObjectProperty(None)
    desar_app_mov_actual = ObjectProperty(None)
    desar_sist_emb_actual = ObjectProperty(None)
    
    app_cs_prev = ObjectProperty(None)
    desar_web_prev = ObjectProperty(None)   
    desar_juegos_prev = ObjectProperty(None) 
    desar_app_mov_prev = ObjectProperty(None) 
    desar_sist_emb_prev = ObjectProperty(None) 


    def submit(self):
        if ((self.app_cs_actual.text in y or self.app_cs_actual.text.count("") == 1) and (self.desar_web_actual.text in y or self.desar_web_actual.text.count("") == 1)
                and (self.desar_juegos_actual.text in y or self.desar_juegos_actual.text.count("") == 1) and (self.desar_app_mov_actual.text in y or self.desar_app_mov_actual.text.count("") == 1)
                and (self.desar_sist_emb_actual.text in y or self.desar_sist_emb_actual.text.count("") == 1) and (self.app_cs_prev.text in y or self.app_cs_prev.text.count("") == 1)
                and (self.desar_web_prev.text in y or self.desar_web_prev.text.count("") == 1) and (self.desar_juegos_prev.text in y or self.desar_juegos_prev.text.count("") == 1)
                and (self.desar_app_mov_prev.text in y or self.desar_app_mov_prev.text.count("") == 1) and (self.desar_sist_emb_prev.text in y or self.desar_sist_emb_prev.text.count("") == 1)):
            x2_11 = fragmentar(self.app_cs_actual.text)
            x2_12 = fragmentar(self.desar_web_actual.text)
            x2_13 = fragmentar(self.desar_juegos_actual.text)
            x2_14 = fragmentar(self.desar_app_mov_actual.text)
            x2_15 = fragmentar(self.desar_sist_emb_actual.text)
            
            x2_21 = fragmentar(self.app_cs_prev.text)
            x2_22 = fragmentar(self.desar_web_prev.text)
            x2_23 = fragmentar(self.desar_juegos_prev.text)
            x2_24 = fragmentar(self.desar_app_mov_prev.text)
            x2_25 = fragmentar(self.desar_sist_emb_prev.text)
            sm.current = "main"
            
            perfil2_dict = {'x2_11':x2_11, 'x2_12':x2_12, 'x2_13':x2_13, 'x2_14':x2_14, 'x2_15':x2_15,
                        'x2_21':x2_21, 'x2_22':x2_22, 'x2_23':x2_23, 'x2_24':x2_24, 'x2_25':x2_25}
            df_perfil2 = pd.DataFrame.from_dict(perfil2_dict)
            df_perfil2.to_csv("perfil2.csv")
            
        else:
            invalidForm()
            sm.current = "perfil2"
    
            self.reset() 
    
            
    def reset(self):
        self.app_cs_actual.text = ""
        self.desar_web_actual.text = ""
        self.desar_juegos_actual.text = ""
        self.desar_app_mov_actual.text = ""  
        self.desar_sist_emb_actual.text = ""          
        
        self.app_cs_prev.text = ""
        self.desar_web_prev.text = ""
        self.desar_juegos_prev.text = ""
        self.desar_app_mov_prev.text = ""  
        self.desar_sist_emb_prev.text = ""  
        
class Perfil3(Screen):
    app_mov_actual = ObjectProperty(None)
    sist_em_actual = ObjectProperty(None)
    
    app_mov_prev = ObjectProperty(None)
    sist_em_prev = ObjectProperty(None)


    def submit(self):
        if ((self.app_mov_actual.text in y or self.app_mov_actual.text.count("") == 1) and (self.app_mov_prev.text in y or self.app_mov_prev.text.count("") == 1)
                and (self.sist_em_actual.text in y or self.sist_em_actual.text.count("") == 1) and (self.sist_em_prev.text in y or self.sist_em_prev.text.count("") == 1)):
            x3_11 = fragmentar(self.app_mov_actual.text)
            x3_12 = fragmentar(self.app_mov_prev.text)
            
            x3_21 = fragmentar(self.sist_em_actual.text)
            x3_22 = fragmentar(self.sist_em_prev.text)
            sm.current = "main"        
          
            perfil3_dict = {'x3_11':x3_11, 'x3_12':x3_12, 'x3_21':x3_21, 'x3_22':x3_22}
            df_perfil3 = pd.DataFrame.from_dict(perfil3_dict)
            df_perfil3.to_csv("perfil3.csv")
            
            self.reset() 
        else:
            invalidForm()
            sm.current = "perfil1"

        
    def reset(self):
        self.app_mov_actual.text = ""
        self.sist_em_actual.text = ""
        
        self.app_mov_prev.text = ""
        self.sist_em_prev.text = ""

class Perfil4(Screen):
    desar_actual = ObjectProperty(None)
    esp_inf_actual = ObjectProperty(None)
    analist_actual = ObjectProperty(None)
    
    desar_prev = ObjectProperty(None)
    esp_inf_prev = ObjectProperty(None)   
    analist_prev = ObjectProperty(None) 

    def submit(self):
        if ((self.desar_actual.text in y or self.desar_actual.text.count("") == 1) and (self.esp_inf_actual.text in y or self.esp_inf_actual.text.count("") == 1)
                and (self.analist_actual.text in y or self.analist_actual.text.count("") == 1) and (self.desar_prev.text in y or self.desar_prev.text.count("") == 1)
                and (self.esp_inf_prev.text in y or self.esp_inf_prev.text.count("") == 1) and (self.analist_prev.text in y or self.analist_prev.text.count("") == 1)):
            
            x4_11 = fragmentar(self.desar_actual.text)
            x4_12 = fragmentar(self.esp_inf_actual.text)
            x4_13 = fragmentar(self.analist_actual.text)
            
            x4_21 = fragmentar(self.desar_prev.text)
            x4_22 = fragmentar(self.esp_inf_prev.text)
            x4_23 = fragmentar(self.analist_prev.text)

            sm.current = "main"
            
            perfil4_dict = {'x4_11':x4_11, 'x4_12':x4_12, 'x4_13':x4_13,
                        'x4_21':x4_21, 'x4_22':x4_22, 'x4_23':x4_23}
            df_perfil4 = pd.DataFrame.from_dict(perfil4_dict)
            df_perfil4.to_csv("perfil4.csv")
            
        else:
            invalidForm()
            sm.current = "perfil4"
    
            self.reset() 
    
            
    def reset(self):
        self.desar_actual.text = ""
        self.esp_inf_actual.text = ""
        self.analist_actual.text = ""
        
        self.desar_prev.text = ""
        self.esp_inf_prev.text = ""   
        self.analist_prev.text = ""         

class Perfil5(Screen):
    ap_erp_crm_actual = ObjectProperty(None)
    esp_proc_actual = ObjectProperty(None)
    esp_ind_actual = ObjectProperty(None)
    
    ap_erp_crm_prev = ObjectProperty(None)
    esp_proc_prev = ObjectProperty(None)   
    esp_ind_prev = ObjectProperty(None)   

    def submit(self):
        if ((self.ap_erp_crm_actual.text in y or self.ap_erp_crm_actual.text.count("") == 1) and (self.esp_proc_actual.text in y or self.esp_proc_actual.text.count("") == 1)
                and (self.esp_ind_actual.text in y or self.esp_ind_actual.text.count("") == 1) and (self.ap_erp_crm_prev.text in y or self.ap_erp_crm_prev.text.count("") == 1)
                and (self.esp_proc_prev.text in y or self.esp_proc_prev.text.count("") == 1) and (self.esp_ind_prev.text in y or self.esp_ind_prev.text.count("") == 1)):
            
            x5_11 = fragmentar(self.ap_erp_crm_actual.text)
            x5_12 = fragmentar(self.esp_proc_actual.text)
            x5_13 = fragmentar(self.esp_ind_actual.text)
            
            x5_21 = fragmentar(self.ap_erp_crm_prev.text)
            x5_22 = fragmentar(self.esp_proc_prev.text)
            x5_23 = fragmentar(self.esp_ind_prev.text)

            sm.current = "main"
            
            perfil5_dict = {'x5_11':x5_11, 'x5_12':x5_12, 'x5_13':x5_13,
                        'x5_21':x5_21, 'x5_22':x5_22, 'x5_23':x5_23}
            df_perfil5 = pd.DataFrame.from_dict(perfil5_dict)
            df_perfil5.to_csv("perfil5.csv")
            
        else:
            invalidForm()
            sm.current = "perfil5"
    
            self.reset() 
    
            
    def reset(self):
        self.ap_erp_crm_actual.text = ""
        self.esp_proc_actual.text = ""
        self.esp_ind_actual.text = ""
        
        self.ap_erp_crm_prev.text = ""
        self.esp_proc_prev.text = ""   
        self.esp_ind_prev.text = ""              


class WindowManager(ScreenManager):
    pass

def invalidForm():
    
    pop = Popup(title='Información incorrecta',
                  content= Label(text='''
                    Porfavor ingrese valores númericos\n
                        en todos los recuadros blancos\n
                Para continuar haga click afuera del recuadro
                                '''),
                  size_hint=(None, None), size=(400, 400))   
    pop.open()

def fragmentar(numero): #funcion para dividir en cinco grupos las respuestas
    if (numero == "" or numero == "0"):
        x = [0,0,0,0,0]
    elif numero != "": 
        div = round(int(numero)/5)
        if div*5 == int(numero):
            x = [div,div,div,div,div]
        elif ((div*4) + (div-1)) == int(numero):
            x = [div,div,div,div,div-1]
        elif ((div*4) + (div-2)) == int(numero):
            x = [div,div,div,div,div-2]            
        elif ((div*4) + (div+1)) == int(numero):
            x = [div,div,div,div,div+1]
        elif ((div*4) + (div+2)) == int(numero):
            x = [div,div,div,div,div+2]            
    return x


kv = Builder.load_file("KvEstructuraV01.kv") #cargamos la estructura del app

sm = WindowManager()

screens = [MainWindow(name="main"), Perfil1(name="perfil1"),Perfil2(name="perfil2"),
           Perfil3(name="perfil3"), Perfil4(name="perfil4"), Perfil5(name="perfil5")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
