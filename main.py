# main.py
from operator import index
import pandas as pd
from kivy.app import App

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

#importamos archivo con funciones de web scraping
from Bases import *
import os # para borrar archivos
import random
import sys
    
#lista para chequear que se ingresen valores númericos en los inputs de la app
x = range(9999)
y = []
for n in x:
    y.append(str(n))

urls = pd.read_excel('LinksNoBorrar.xlsx')

class Introduccion(Screen):
    def perfil_csv(self):
    #Creamos .csv de perfiles
        #perfil 1
        data1 = {'x1_11':([0]*len(urls)), 'x1_12':([0]*len(urls))}
        df_data1 = pd.DataFrame.from_dict(data1)
        df_data1.to_csv("perfil1.csv")
        #perfil 2
        data2 = {'x2_11':([0]*len(urls)), 'x2_12':([0]*len(urls)), 'x2_13':([0]*len(urls)), 'x2_14':([0]*len(urls)), 'x2_15':([0]*len(urls))}
        df_data2 = pd.DataFrame.from_dict(data2)
        df_data2.to_csv("perfil2.csv")
        #perfil3
        data3 = {'x3_11':([0]*len(urls)), 'x3_12':([0]*len(urls))}
        df_data3 = pd.DataFrame.from_dict(data3)
        df_data3.to_csv("perfil3.csv")
        #perfil4
        data4 = {'x4_11':([0]*len(urls)), 'x4_12':([0]*len(urls)), 'x4_13':([0]*len(urls))}
        df_data4 = pd.DataFrame.from_dict(data4)
        df_data4.to_csv("perfil4.csv")
        #perfil5
        data5 = {'x5_11':([0]*len(urls)), 'x5_12':([0]*len(urls)), 'x5_13':([0]*len(urls))}
        df_data5 = pd.DataFrame.from_dict(data5)
        df_data5.to_csv("perfil5.csv")
        #perfil6
        data6 = {'x6_11':([0]*len(urls)), 'x6_12':([0]*len(urls)), 'x6_13':([0]*len(urls))}
        df_data6 = pd.DataFrame.from_dict(data6)
        df_data6.to_csv("perfil6.csv")
        #perfil7
        data7 = {'x7_11':([0]*len(urls)), 'x7_12':([0]*len(urls)), 'x7_13':([0]*len(urls)), 'x7_14':([0]*len(urls))}
        df_data7 = pd.DataFrame.from_dict(data7)
        df_data7.to_csv("perfil7.csv")
        #perfil8
        data8 = {'x8_11':([0]*len(urls)), 'x8_12':([0]*len(urls)), 'x8_13':([0]*len(urls))}
        df_data8 = pd.DataFrame.from_dict(data8)
        df_data8.to_csv("perfil8.csv")
        #perfil9
        data9 = {'x9_11':([0]*len(urls)), 'x9_12':([0]*len(urls)), 'x9_13':([0]*len(urls))}
        df_data9 = pd.DataFrame.from_dict(data9)
        df_data9.to_csv("perfil9.csv")
        #perfil10
        data10 = {'x10_11':([0]*len(urls)), 'x10_12':([0]*len(urls)), 'x10_13':([0]*len(urls)), 'x10_14':([0]*len(urls)), 'x10_15':([0]*len(urls)), 'x10_16':([0]*len(urls))}
        df_data10 = pd.DataFrame.from_dict(data10)
        df_data10.to_csv("perfil10.csv")
        #perfil11
        data11 = {'x11_11':([0]*len(urls))}
        df_data11 = pd.DataFrame.from_dict(data11)
        df_data11.to_csv("perfil11.csv")
        #perfil12
        data12 = {'x12_11':([0]*len(urls))}
        df_data12 = pd.DataFrame.from_dict(data12)
        df_data12.to_csv("perfil12.csv")
        #perfil13
        data13 = {'x13_11':([0]*len(urls))}
        df_data13 = pd.DataFrame.from_dict(data13)
        df_data13.to_csv("perfil13.csv")
        #perfil14
        data14 = {'x14_11':([0]*len(urls))}
        df_data14 = pd.DataFrame.from_dict(data14)
        df_data14.to_csv("perfil14.csv")
        #perfil15
        data15 = {'x15_11':([0]*len(urls))}
        df_data15 = pd.DataFrame.from_dict(data15)
        df_data15.to_csv("perfil15.csv")
        #perfil16
        data16 = {'x16_11':([0]*len(urls))}
        df_data16 = pd.DataFrame.from_dict(data16)
        df_data16.to_csv("perfil16.csv")
        #perfil17
        data17 = {'x17_11':([0]*len(urls))}
        df_data17 = pd.DataFrame.from_dict(data17)
        df_data17.to_csv("perfil17.csv")
        #perfil18
        data18 = {'x18_11':([0]*len(urls))}
        df_data18 = pd.DataFrame.from_dict(data18)
        df_data18.to_csv("perfil18.csv")

class MainWindow(Screen):
    def btn(self):
        mensaje_final()

class Popups(FloatLayout):
    def fin(self):
        p1 = pd.read_csv('perfil1.csv') #respuestas a la primera pregunta
        p2 = pd.read_csv('perfil2.csv') #respuestas a la segunda pregunta
        p3 = pd.read_csv('perfil3.csv') #respuestas a la segunda pregunta
        p4 = pd.read_csv('perfil4.csv') #respuestas a la segunda pregunta
        p5 = pd.read_csv('perfil5.csv') #respuestas a la segunda pregunta
        p6 = pd.read_csv('perfil6.csv') #respuestas a la segunda pregunta
        p7 = pd.read_csv('perfil7.csv') #respuestas a la segunda pregunta
        p8 = pd.read_csv('perfil8.csv') #respuestas a la segunda pregunta
        p9 = pd.read_csv('perfil9.csv') #respuestas a la primera pregunta
        p10 = pd.read_csv('perfil10.csv') #respuestas a la segunda pregunta
        p11 = pd.read_csv('perfil11.csv') #respuestas a la segunda pregunta
        p12 = pd.read_csv('perfil12.csv') #respuestas a la segunda pregunta
        p13 = pd.read_csv('perfil13.csv') #respuestas a la segunda pregunta
        p14 = pd.read_csv('perfil14.csv') #respuestas a la segunda pregunta
        p15 = pd.read_csv('perfil15.csv') #respuestas a la segunda pregunta
        p16 = pd.read_csv('perfil16.csv') #respuestas a la segunda pregunta    
        p17 = pd.read_csv('perfil17.csv') #respuestas a la segunda pregunta
        p18 = pd.read_csv('perfil18.csv') #respuestas a la segunda pregunta     
        urls = pd.read_excel('LinksNoBorrar.xlsx') 
        urls = urls.links.sample(frac = 1).reset_index(drop=True) #orden aleatorio de links
        urls = urls.to_frame() 
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_window_position(-10000,0) # escondemos el web driver
        
        #loopeamos por la cantidad de respuestas en el df
        for user_id in range(len(urls)):
            driver.get(urls.links[user_id])
            driver = answers(driver = driver, df = p1, rta1 = rta1, rta2 = rta2, user_id = user_id)
            driver = answers2(driver = driver, df = p2, rta2a = rta2_a, rta2b = rta2_b,
                        rta2c = rta2_c, rta2d = rta2_d, rta2e = rta2_e, user_id = user_id)
            driver = answers3(driver = driver, df = p3, rta3a = rta3_a, rta3b = rta3_b, user_id = user_id)
            driver = answers4(driver = driver, df = p4, rta4a = rta4_a, rta4b = rta4_b, rta4c = rta4_c, user_id = user_id)
            driver = answers5(driver = driver, df = p5, rta5a = rta5_a, rta5b = rta5_b, rta5c = rta5_c, user_id = user_id)
            driver = answers6(driver = driver, df = p6, rta6a = rta6_a, rta6b = rta6_b, rta6c = rta6_c, user_id = user_id)
            driver = answers7(driver = driver, df = p7, rta7a = rta7_a, rta7b = rta7_b,
                        rta7c = rta7_c, rta7d = rta7_d, user_id = user_id)
            driver = answers8(driver = driver, df = p8, rta8a = rta8_a, rta8b = rta8_b, rta8c = rta8_c, user_id = user_id)
            driver = answers9(driver = driver, df = p9, rta9a = rta9_a, rta9b = rta9_b, rta9c = rta9_c, user_id = user_id)
            driver = answers10(driver = driver, df = p10, rta10a = rta10_a, rta10b = rta10_b,
                        rta10c = rta10_c, rta10d = rta10_d, rta10e = rta10_e, rta10f = rta10_f, user_id = user_id)
            driver = answers11(driver = driver, df = p11, rta11a = rta11_a, user_id = user_id)
            driver = answers12(driver = driver, df = p12, rta12a = rta12_a, user_id = user_id)
            driver = answers13(driver = driver, df = p13, rta13a = rta13_a, user_id = user_id)
            driver = answers14(driver = driver, df = p14, rta14a = rta14_a, user_id = user_id)
            driver = answers15(driver = driver, df = p15, rta15a = rta15_a, user_id = user_id)
            driver = answers16(driver = driver, df = p16, rta16a = rta16_a, user_id = user_id)
            driver = answers17(driver = driver, df = p17, rta17a = rta17_a, user_id = user_id)
            driver = answers18(driver = driver, df = p18, rta18a = rta18_a, user_id = user_id)
            driver = submit(driver = driver, element_class = submit_class)            

        driver.close() # cerramos el web driver
        perfiles = ["perfil1.csv", "perfil2.csv", "perfil3.csv", "perfil4.csv", "perfil5.csv", "perfil6.csv",
                    "perfil7.csv", "perfil8.csv", "perfil9.csv", "perfil10.csv", "perfil11.csv", "perfil12.csv",
                    "perfil13.csv", "perfil14.csv", "perfil15.csv", "perfil16.csv", "perfil17.csv", "perfil18.csv"]
        for perfil in perfiles:
            os.remove(perfil)

        FormularioTECx.get_running_app().stop()
       
class Perfil1(Screen): #Líder de Desarrollo / Proyect Manager (PM)
    pm = ObjectProperty(None)
    sdm = ObjectProperty(None)
    
    def submit(self):
        if ((self.pm.text in y or self.pm.text.count("") == 1) and (self.sdm.text in y or self.sdm.text.count("") == 1) ):
            x1_11 = fragmentar(self.pm.text)
            x1_12 = fragmentar(self.sdm.text)
        
            sm.current = "main"        
          
            perfil1_dict = {'x1_11':x1_11, 'x1_12':x1_12}
            df_perfil1 = pd.DataFrame.from_dict(perfil1_dict)
            df_perfil1.to_csv("perfil1.csv")

        else:
            invalidForm()
            sm.current = "perfil1"
            self.reset()
    def reset(self):
        self.pm.text = ""
        self.sdm.text = ""

class Perfil2(Screen): #Desarrollador de Software
    app_cs = ObjectProperty(None)
    desar_web = ObjectProperty(None)
    desar_juegos = ObjectProperty(None)
    desar_app_mov = ObjectProperty(None)
    desar_sist_emb = ObjectProperty(None)

    def submit(self):
        if ((self.app_cs.text in y or self.app_cs.text.count("") == 1) and (self.desar_web.text in y or self.desar_web.text.count("") == 1)
                and (self.desar_juegos.text in y or self.desar_juegos.text.count("") == 1) and (self.desar_app_mov.text in y or self.desar_app_mov.text.count("") == 1)
                and (self.desar_sist_emb.text in y or self.desar_sist_emb.text.count("") == 1)):
            x2_11 = fragmentar(self.app_cs.text)
            x2_12 = fragmentar(self.desar_web.text)
            x2_13 = fragmentar(self.desar_juegos.text)
            x2_14 = fragmentar(self.desar_app_mov.text)
            x2_15 = fragmentar(self.desar_sist_emb.text)
            sm.current = "main"
            
            perfil2_dict = {'x2_11':x2_11, 'x2_12':x2_12, 'x2_13':x2_13, 'x2_14':x2_14, 'x2_15':x2_15}
            df_perfil2 = pd.DataFrame.from_dict(perfil2_dict)
            df_perfil2.to_csv("perfil2.csv")

        else:
            invalidForm()
            sm.current = "perfil2"
            self.reset() 
    def reset(self):
        self.app_cs.text = ""
        self.desar_web.text = ""
        self.desar_juegos.text = ""
        self.desar_app_mov.text = ""  
        self.desar_sist_emb.text = ""          

class Perfil3(Screen): #Arquitecto de Software
    app_mov = ObjectProperty(None)
    sist_em = ObjectProperty(None)

    def submit(self):
        if ((self.app_mov.text in y or self.app_mov.text.count("") == 1) and (self.sist_em.text in y or self.sist_em.text.count("") == 1)):
            x3_11 = fragmentar(self.app_mov.text)         
            x3_12 = fragmentar(self.sist_em.text)

            sm.current = "main"        
          
            perfil3_dict = {'x3_11':x3_11, 'x3_12':x3_12}
            df_perfil3 = pd.DataFrame.from_dict(perfil3_dict)
            df_perfil3.to_csv("perfil3.csv")

        else:
            invalidForm()
            sm.current = "perfil3"
            self.reset()
    def reset(self):
        self.app_mov.text = ""
        self.sist_em.text = ""

class Perfil4(Screen): #Consultor BI - Business Intelligence
    desar = ObjectProperty(None)
    esp_inf = ObjectProperty(None)
    analist = ObjectProperty(None)

    def submit(self):
        if ((self.desar.text in y or self.desar.text.count("") == 1) and (self.esp_inf.text in y or self.esp_inf.text.count("") == 1)
                and (self.analist.text in y or self.analist.text.count("") == 1)):
            
            x4_11 = fragmentar(self.desar.text)
            x4_12 = fragmentar(self.esp_inf.text)
            x4_13 = fragmentar(self.analist.text)

            sm.current = "main"
            
            perfil4_dict = {'x4_11':x4_11, 'x4_12':x4_12, 'x4_13':x4_13}
            df_perfil4 = pd.DataFrame.from_dict(perfil4_dict)
            df_perfil4.to_csv("perfil4.csv")

        else:
            invalidForm()
            sm.current = "perfil4"
            self.reset() 
    def reset(self):
        self.desar.text = ""
        self.esp_inf.text = ""
        self.analist.text = ""

class Perfil5(Screen): #Analista de Negocios
    ap_erp_crm = ObjectProperty(None)
    esp_proc = ObjectProperty(None)
    esp_ind = ObjectProperty(None)

    def submit(self):
        if ((self.ap_erp_crm.text in y or self.ap_erp_crm.text.count("") == 1) and (self.esp_proc.text in y or self.esp_proc.text.count("") == 1)
                and (self.esp_ind.text in y or self.esp_ind.text.count("") == 1)):
            
            x5_11 = fragmentar(self.ap_erp_crm.text)
            x5_12 = fragmentar(self.esp_proc.text)
            x5_13 = fragmentar(self.esp_ind.text)

            sm.current = "main"
            
            perfil5_dict = {'x5_11':x5_11, 'x5_12':x5_12, 'x5_13':x5_13}
            df_perfil5 = pd.DataFrame.from_dict(perfil5_dict)
            df_perfil5.to_csv("perfil5.csv")
            
        else:
            invalidForm()
            sm.current = "perfil5"
            self.reset() 
    def reset(self):
        self.ap_erp_crm.text = ""
        self.esp_proc.text = ""
        self.esp_ind.text = ""

class Perfil6(Screen): #Diseñador Web
    uxd = ObjectProperty(None)
    webd = ObjectProperty(None)
    mkt = ObjectProperty(None)

    def submit(self):
        if ((self.uxd.text in y or self.uxd.text.count("") == 1) and (self.webd.text in y or self.webd.text.count("") == 1)
                and (self.mkt.text in y or self.mkt.text.count("") == 1)):
            
            x6_11 = fragmentar(self.uxd.text)
            x6_12 = fragmentar(self.webd.text)
            x6_13 = fragmentar(self.mkt.text)

            sm.current = "main"
            
            perfil6_dict = {'x6_11':x6_11, 'x6_12':x6_12, 'x6_13':x6_13}
            df_perfil6 = pd.DataFrame.from_dict(perfil6_dict)
            df_perfil6.to_csv("perfil6.csv")
            
        else:
            invalidForm()
            sm.current = "perfil6"
            self.reset() 
    def reset(self):
        self.uxd.text = ""
        self.webd.text = ""
        self.mkt.text = ""  

class Perfil7(Screen): #Analista UX (Usabilidad)
    research = ObjectProperty(None)
    analisis = ObjectProperty(None)
    prot_inter = ObjectProperty(None)
    test_us = ObjectProperty(None)

    def submit(self):
        if ((self.research.text in y or self.research.text.count("") == 1) and (self.analisis.text in y or self.analisis.text.count("") == 1)
                and (self.prot_inter.text in y or self.prot_inter.text.count("") == 1) and (self.test_us.text in y or self.test_us.text.count("") == 1)):

            x7_11 = fragmentar(self.research.text)
            x7_12 = fragmentar(self.analisis.text)
            x7_13 = fragmentar(self.prot_inter.text)
            x7_14 = fragmentar(self.test_us.text)

            sm.current = "main"
            
            perfil7_dict = {'x7_11':x7_11, 'x7_12':x7_12, 'x7_13':x7_13, 'x7_14':x7_14}
            df_perfil7 = pd.DataFrame.from_dict(perfil7_dict)
            df_perfil7.to_csv("perfil7.csv")
            
        else:
            invalidForm()
            sm.current = "perfil7"
            self.reset() 
    def reset(self):
        self.research.text = ""
        self.analisis.text = ""
        self.prot_inter.text = ""
        self.test_us.text = ""  

class Perfil8(Screen): #Tester / Analista Tester
    orient_tec = ObjectProperty(None)
    orient_func = ObjectProperty(None)
    orient_seg = ObjectProperty(None)

    def submit(self):
        if ((self.orient_tec.text in y or self.orient_tec.text.count("") == 1) and (self.orient_func.text in y or self.orient_func.text.count("") == 1)
                and (self.orient_seg.text in y or self.orient_seg.text.count("") == 1)):
            
            x8_11 = fragmentar(self.orient_tec.text)
            x8_12 = fragmentar(self.orient_func.text)
            x8_13 = fragmentar(self.orient_seg.text)

            sm.current = "main"
            
            perfil8_dict = {'x8_11':x8_11, 'x8_12':x8_12, 'x8_13':x8_13}
            df_perfil8 = pd.DataFrame.from_dict(perfil8_dict)
            df_perfil8.to_csv("perfil8.csv")
            
        else:
            invalidForm()
            sm.current = "perfil8"
            self.reset() 
    def reset(self):
        self.orient_tec.text = ""
        self.orient_func.text = ""
        self.orient_seg.text = ""

class Perfil9(Screen): #Analista de Calidad
    iso = ObjectProperty(None)
    itil = ObjectProperty(None)
    cmmi = ObjectProperty(None)

    def submit(self):
        if ((self.iso.text in y or self.iso.text.count("") == 1) and (self.itil.text in y or self.itil.text.count("") == 1)
                and (self.cmmi.text in y or self.cmmi.text.count("") == 1)):
            
            x9_11 = fragmentar(self.iso.text)
            x9_12 = fragmentar(self.itil.text)
            x9_13 = fragmentar(self.cmmi.text)

            sm.current = "main"
            
            perfil9_dict = {'x9_11':x9_11, 'x9_12':x9_12, 'x9_13':x9_13}
            df_perfil9 = pd.DataFrame.from_dict(perfil9_dict)
            df_perfil9.to_csv("perfil9.csv")
            
        else:
            invalidForm()
            sm.current = "perfil9"
            self.reset() 
    def reset(self):
        self.iso.text = ""
        self.itil.text = ""
        self.cmmi.text = ""

class Perfil10(Screen): #IT Manager
    datcenter = ObjectProperty(None)
    rout_switch = ObjectProperty(None)
    video = ObjectProperty(None)
    voice = ObjectProperty(None)
    redes = ObjectProperty(None)
    seg = ObjectProperty(None)

    def submit(self):
        if ((self.datcenter.text in y or self.datcenter.text.count("") == 1) and (self.rout_switch.text in y or self.rout_switch.text.count("") == 1)
                and (self.video.text in y or self.video.text.count("") == 1) and (self.voice.text in y or self.voice.text.count("") == 1)
                and (self.redes.text in y or self.redes.text.count("") == 1) and (self.seg.text in y or self.seg.text.count("") == 1)):
            x10_11 = fragmentar(self.datcenter.text)
            x10_12 = fragmentar(self.rout_switch.text)
            x10_13 = fragmentar(self.video.text)
            x10_14 = fragmentar(self.voice.text)
            x10_15 = fragmentar(self.redes.text)
            x10_16 = fragmentar(self.seg.text)

            sm.current = "main"
            
            perfil10_dict = {'x10_11':x10_11, 'x10_12':x10_12, 'x10_13':x10_13, 'x10_14':x10_14, 'x10_15':x10_15, 'x10_16':x10_16}
            df_perfil10 = pd.DataFrame.from_dict(perfil10_dict)
            df_perfil10.to_csv("perfil10.csv")
            
        else:
            invalidForm()
            sm.current = "perfil10"
            self.reset() 
    def reset(self):
        self.datcenter.text = ""
        self.rout_switch.text = ""
        self.video.text = ""
        self.voice.text = ""  
        self.redes.text = ""
        self.seg.text = ""    

class Perfil11(Screen): #Administrador de Base de Datos (DBA)
    dba = ObjectProperty(None)
    
    def submit(self):
        if ((self.dba.text in y or self.dba.text.count("") == 1)):
            x11_11 = fragmentar(self.dba.text)
        
            sm.current = "main"        
          
            perfil11_dict = {'x11_11':x11_11}
            df_perfil11 = pd.DataFrame.from_dict(perfil11_dict)
            df_perfil11.to_csv("perfil11.csv")

        else:
            invalidForm()
            sm.current = "perfil11"
            self.reset()
    def reset(self):
        self.dba.text = ""

class Perfil12(Screen): #Analista Funcional
    afunc = ObjectProperty(None)
    
    def submit(self):
        if ((self.afunc.text in y or self.afunc.text.count("") == 1)):
            x12_11 = fragmentar(self.afunc.text)
        
            sm.current = "main"        
          
            perfil12_dict = {'x12_11':x12_11}
            df_perfil12 = pd.DataFrame.from_dict(perfil12_dict)
            df_perfil12.to_csv("perfil12.csv")
 
        else:
            invalidForm()
            sm.current = "perfil12"
            self.reset()
    def reset(self):
        self.afunc.text = ""

class Perfil13(Screen): #Analista Big Data - Data Scientist
    dscience = ObjectProperty(None)
    
    def submit(self):
        if ((self.dscience.text in y or self.dscience.text.count("") == 1)):
            x13_11 = fragmentar(self.dscience.text)
        
            sm.current = "main"        
          
            perfil13_dict = {'x13_11':x13_11}
            df_perfil13 = pd.DataFrame.from_dict(perfil13_dict)
            df_perfil13.to_csv("perfil13.csv")

        else:
            invalidForm()
            sm.current = "perfil13"
            self.reset()
    def reset(self):
        self.dscience.text = ""

class Perfil14(Screen): #Analista Middleware
    midd = ObjectProperty(None)
    
    def submit(self):
        if ((self.midd.text in y or self.midd.text.count("") == 1)):
            x14_11 = fragmentar(self.midd.text)
        
            sm.current = "main"        
          
            perfil14_dict = {'x14_11':x14_11}
            df_perfil14 = pd.DataFrame.from_dict(perfil14_dict)
            df_perfil14.to_csv("perfil14.csv")

        else:
            invalidForm()
            sm.current = "perfil14"
            self.reset()
    def reset(self):
        self.midd.text = ""

class Perfil15(Screen): #Soporte Técnico
    soporte = ObjectProperty(None)
    
    def submit(self):
        if ((self.soporte.text in y or self.soporte.text.count("") == 1)):
            x15_11 = fragmentar(self.soporte.text)
        
            sm.current = "main"        
          
            perfil15_dict = {'x15_11':x15_11}
            df_perfil15 = pd.DataFrame.from_dict(perfil15_dict)
            df_perfil15.to_csv("perfil15.csv")

        else:
            invalidForm()
            sm.current = "perfil15"
            self.reset()
    def reset(self):
        self.soporte.text = ""

class Perfil16(Screen): #Especialista en Seguridad de la Información
    esp_seg = ObjectProperty(None)
    
    def submit(self):
        if ((self.esp_seg.text in y or self.esp_seg.text.count("") == 1)):
            x16_11 = fragmentar(self.esp_seg.text)
        
            sm.current = "main"        
          
            perfil16_dict = {'x16_11':x16_11}
            df_perfil16= pd.DataFrame.from_dict(perfil16_dict)
            df_perfil16.to_csv("perfil16.csv")
 
        else:
            invalidForm()
            sm.current = "perfil16"
            self.reset() 
    def reset(self):
        self.esp_seg.text = ""

class Perfil17(Screen): #Implementador Configuration Manager
    config = ObjectProperty(None)

    def submit(self):
        if ((self.config.text in y or self.config.text.count("") == 1)):
            x17_11 = fragmentar(self.config.text)
        
            sm.current = "main"        
          
            perfil17_dict = {'x17_11':x17_11}
            df_perfil17= pd.DataFrame.from_dict(perfil17_dict)
            df_perfil17.to_csv("perfil17.csv")
            
        else:
            invalidForm()
            sm.current = "perfil17"
            self.reset() 
    def reset(self):
        self.config.text = ""

class Perfil18(Screen): #Implementador Software de Gestión
    soft_gest = ObjectProperty(None)

    def submit(self):
        if ((self.soft_gest.text in y or self.soft_gest.text.count("") == 1)):
            x18_11 = fragmentar(self.soft_gest.text)
        
            sm.current = "main"        
          
            perfil18_dict = {'x18_11':x18_11}
            df_perfil18= pd.DataFrame.from_dict(perfil18_dict)
            df_perfil18.to_csv("perfil18.csv")

        else:
            invalidForm()
            sm.current = "perfil18"
            self.reset() 
    def reset(self):
        self.soft_gest.text = ""

class WindowManager(ScreenManager):
    pass

### Funciones
def invalidForm():
    
    pop = Popup(title='Información incorrecta',
                  content= Label(text='''
                    Porfavor ingrese valores númericos\n
                        en todos los recuadros blancos\n
                 Para continuar haga click afuera del recuadro
                                '''),
                  size_hint=( 0.6, 0.3), size=(400, 300))
                  
    pop.open()

def mensaje_final():  
    show = Popups()
  
    pop_final = Popup(title ="Envío de respuestas", content = show,
        size_hint=(None, None), size=(400, 300))   

    pop_final.open()   

def fragmentar(numero, cant_url = len(urls)): #funcion para dividir en cinco grupos las respuestas
    if (numero == "" or numero == "0"):
        x = [0] * cant_url
    elif numero != "":
        raiz = int(numero) / cant_url # len(cant_url)
        if raiz < 10:
            aleatorios = [random.uniform(raiz, -raiz) for i in range(cant_url)]
        else:
            aleatorios = [random.uniform(10, -10) for i in range(cant_url)]
        num_fragmentado = [0] * cant_url # len(cant_url)
        for i in range(0,len(aleatorios)):
            num_fragmentado[i] = round(raiz + aleatorios[i])
        suma_fragmentada = sum(num_fragmentado)
        exced_falt = (int(numero) - suma_fragmentada) 
        if exced_falt >= 0:
            num_fragmentado[0] = num_fragmentado[0] + exced_falt
        elif exced_falt < 0:
            if abs(exced_falt) <= num_fragmentado[0]:
                num_fragmentado[0] = num_fragmentado[0] + exced_falt
            else:
                exced_falt = exced_falt + num_fragmentado[0]
                num_fragmentado[0] = 0
                if (abs(exced_falt) <= num_fragmentado[1]) and (abs(exced_falt) != 0):
                    num_fragmentado[1] = num_fragmentado[1] + exced_falt
                elif abs(exced_falt) > num_fragmentado[1]:
                    exced_falt = exced_falt + num_fragmentado[1]
                    num_fragmentado[1] = 0
        x = []
        for i in range(0,cant_url):
            x.append(num_fragmentado[i])
    return x

kv = Builder.load_file("KvEstructura.kv") #cargamos la estructura del app

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("TECx.png")

sm = WindowManager()
screens = [Introduccion(name="intro") , MainWindow(name="main"), Perfil1(name="perfil1"), 
            Perfil2(name="perfil2"), Perfil3(name="perfil3"), Perfil4(name="perfil4"), 
            Perfil5(name="perfil5"), Perfil6(name="perfil6"), Perfil7(name="perfil7"), 
            Perfil8(name="perfil8"), Perfil9(name="perfil9"), Perfil10(name="perfil10"), 
            Perfil11(name="perfil11"), Perfil12(name="perfil12"), Perfil13(name="perfil13"), 
            Perfil14(name="perfil14"), Perfil15(name="perfil15"), Perfil16(name="perfil16"), 
            Perfil17(name="perfil17"), Perfil18(name="perfil18")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "intro"

class FormularioTECx(App):
    def build(self):
        self.icon = 'TECx.png'
        return sm

if __name__ == "__main__":
    FormularioTECx().run()
