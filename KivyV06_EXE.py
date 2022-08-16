# main.py

print("")
print("")
print("Por favor, espere hasta que terminen de cargarse las librerías necesarias")

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
#from Bases import *
import os # para borrar archivos
import random
import sys
import glob

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("TECx.png")

Builder.load_string("""
<Introduccion>:
    name: "intro"
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
                text: "[u]Monitor Estadístico TECx[/u]"
                markup: True
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4 / 2

            Label:
                text: "Esta aplicación trabaja con un algoritmo que fragmenta las respuestas para"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.9}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2    

            Label:
                text: "completar con ellas distintos formularios electrónicos que impidan reconstruir los"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.85}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2       

            Label:
                text: "datos ingresados por su empresa. De esta manera está garantizado el anonimato."
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.8}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2                  

            Label:
                text: "En esta primera medición, el objetivo es relevar los perfiles de RRHH transversales a todos"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2   

            Label:
                text: "los segmentos de la economía del conocimiento. Para próximas mediciones se trabajará con "
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 15.5**4     /2                                                               
                
            Label:
                text: "cada segmento en la medición de RRHH específicos."
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.65}
                font_size: (root.width**2 + root.height**2) / 15.5**4       /2                              
                
            Label:
                text: "Al seleccionar la opción continuar aparecerá una botonera con cada perfil de RRHH."
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.4}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2

            Label:
                text: "Podrá ingresar a cualquier perfil. Podrá dejar campos en blanco."
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.35}
                font_size: (root.width**2 + root.height**2) / 15.5**4        /2      

            Label:
                text: "Podrá, también, regresar y modificar datos."
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.3}
                font_size: (root.width**2 + root.height**2) / 15.5**4       /2

            Label:
                text: "Desarrollado por EconomicTrends"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.1}
                font_size: (root.width**2 + root.height**2) / 17**4    /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.8, 0.17
            text: "Continuar al formulario"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
                root.perfil_csv()            
            on_release:
                app.root.current = "main"                  
                root.manager.transition.direction = "left"   


<MainWindow>:
    name: "main"
    GridLayout:
        cols:1
        canvas.before:
            Color:
                rgba:(0/255,51/255,102/255,1)
            Rectangle:
                pos:self.pos
                size:self.size
        GridLayout:
            cols:2                
            Button:
                text: "Líder de Desarrollo / Proyect Manager / SDM / Scrum Master"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil1"
                    root.manager.transition.direction = "left"
            Button:
                text: "Cloud Engineer"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil1b"
                    root.manager.transition.direction = "left"                    
            Button:
                text: "Desarrollador de Software Back End"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil2a"
                    root.manager.transition.direction = "left"  
            Button:
                text: "Desarrollador de Software Front End"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil2b"
                    root.manager.transition.direction = "left"
            Button:
                text: "Desarrollador de Software Full Stack"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil2c"
                    root.manager.transition.direction = "left"                                        
            Button:
                text: "Arquitecto de Software"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil3"
                    root.manager.transition.direction = "left" 
            Button:
                text: "Consultor BI - Business Intelligence"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil4"
                    root.manager.transition.direction = "left" 
            Button:
                text: "Analista de negocios"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil5"
                    root.manager.transition.direction = "left"   
            Button:
                text: "Diseñador Web"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil6"
                    root.manager.transition.direction = "left"        
            Button:
                text: "Analista UI/UX (usabilidad)"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil7"
                    root.manager.transition.direction = "left"      
            Button:
                text: "Tester / Analista tester"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil8"
                    root.manager.transition.direction = "left"    
            Button:
                text: "QA Automation"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil19"
                    root.manager.transition.direction = "left"                        
            Button:
                text: "Analista de Calidad"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil9"
                    root.manager.transition.direction = "left"    
            Button:
                text: "IT Manager"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil10"
                    root.manager.transition.direction = "left"    
            Button:
                text: "Administardor de Base de Datos (DBA)"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil11"
                    root.manager.transition.direction = "left"        
            Button:
                text: "Analista Funcional"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil12"
                    root.manager.transition.direction = "left"    
            Button:
                text: "Analista Big Data - Data Scientist"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil13"
                    root.manager.transition.direction = "left"  
            Button:
                text: "Experto en Machine Learning"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil21"
                    root.manager.transition.direction = "left"                           
            Button:
                text: "Analista Middleware"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil14"
                    root.manager.transition.direction = "left"
            Button:
                text: "Soporte Técnico"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil15"
                    root.manager.transition.direction = "left"        
            Button:
                text: "Especialista en Seguridad de la Información"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil16"
                    root.manager.transition.direction = "left"    
            Button:
                text: "Implementador Configuration Manager"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil17"
                    root.manager.transition.direction = "left"        
            Button:
                text: "Implementador Software de Gestión"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil18"
                    root.manager.transition.direction = "left"      
            Button:
                text: "DevOps"
                on_press: 
                    self.background_color = (0/255,51/255,102/255,1)
                on_release:
                    app.root.current = "perfil20"
                    root.manager.transition.direction = "left" 

        Button:
            text: "Cerrar APP y Enviar Respuestas"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            size_hint: 0.2, 0.2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                on_release: root.btn()


<Popups>:    
    Label:
        text: "A continuación se hará el envío de sus respuestas." 
        size_hint: 0.6, 0.3
        pos_hint: {"x":0.2, "top":0.99}

    Label:
        text: "Esto puede demorar entre 1 y 2 minutos,"  
        size_hint: 0.6, 0.3
        pos_hint: {"x":0.2, "top":0.89}

    Label:
        text: "por favor no cierre el aplicativo." 
        size_hint: 0.6, 0.3
        pos_hint: {"x":0.2, "top":0.79}        
        
    Button:
        text: "Continuar"
        # set size of the button
        size_hint: 1, 0.4
        # set position of the button  
        pos_hint: {"x":0, "y":0.1}
        on_press: 
            self.background_color = (0/255,51/255,102/255,1)
        on_release:    
            root.fin()

<Perfil1>: #Líder de Desarrollo / Proyect Manager (PM)
    name: "perfil1"
    pm: pm
    sdm: sdm
    scr: scr

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
                text: "Líder de Desarrollo / Proyect Manager (PM)"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "[u]Otras denominaciones[/u]: SDM (Service Delivery Manager)"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4       /2

            Label:
                text: "[u]Misión[/u]: Lograr que el proyecto se desarrolle dentro de los alcances, costos y calidad establecidos en los plazos previstos con la menor"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4        /2     

            Label:
                text: "cantidad de inconvenientes, anticipando posibles problemas o desvíos y tomando decisiones correctivas o proponiendo alternativas a la gerencia"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4        /2                            
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4     /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4             /2      
                            
            Label:
                text: "Gerente de Proyectos o PM:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: pm
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4    /2
       
            Label:
                text: "Gerente de Operaciones de un Cliente / Service Delivery Manager:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: sdm
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Scrum Master / Agile Coach:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*3}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: scr
                pos_hint: {"x":0.8, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2         

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()
                
<Perfil1b>: #Cloud Engineer
    name: "perfil1b"
    name: "perfil1b"
    ceng: ceng

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
                text: "Cloud Engineer"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "[u]Otras denominaciones[/u]: Cloud Consultant / Cloud Administrator / Cloud Specialist / Cloud Analyst"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4         /2              
    
            Label:
                text: "[u]Misión[/u]: Diseñar, implementar y mantener infraestructuras en la nube."
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4       /2                      

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4    /2            
                            
            Label:
                text: "Cloud Engineer:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4 /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: ceng
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2
        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()                 

<Perfil2a>: #Desarrollador de Software Back End
    name: "perfil2a"
    app_cs: app_cs
    desar_web: desar_web
    desar_juegos: desar_juegos
    desar_app_mov: desar_app_mov
    desar_sist_emb: desar_sist_emb

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
                text: "Desarrollador de Software Back End"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "[u]Otras denominaciones[/u]: Programador Back End / Analista-programador Back End / Developer Back End"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4        /2 

            Label:
                text: "[u]Misión[/u]: Participar del proceso de programación / implementación teniendo como entrada las especificaciones de software y ajustándose"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4        /2        

            Label:
                text: " a tiempos y estándares de calidad y trabajo de la organización y del proyecto, ocupándose de la arquitectura interna  de la web, aplicación o software."
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4        /2                             
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4    /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4      /2          
                            
            Label:
                text: "Desarrollador de aplicaciones cliente-servidor:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: app_cs
                pos_hint: {"x":0.8, "top":0.75-0.125}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2
       
            Label:
                text: "Desarrollador Web:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_web
                pos_hint: {"x":0.8, "top":0.75-0.125*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4    /2

            Label:
                text: "Desarrollador de juegos / Aplicaciones lúdicas:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: desar_juegos
                pos_hint: {"x":0.8, "top":0.75-0.125*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4    /2
    
            Label:
                text: "Desarrollador de Aplicaciones Móviles:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*4}                
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_app_mov
                pos_hint: {"x":0.8, "top":0.75-0.125*4}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Desarrollador de Sistemas Embebidos:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*5}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_sist_emb
                pos_hint: {"x":0.8, "top":0.75-0.125*5}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1) 
            on_release:            
                root.manager.transition.direction = "right" 
                root.submit()
   
<Perfil2b>: #Desarrollador de Software Front End
    name: "perfil2b"
    app_cs_b: app_cs_b
    desar_web_b: desar_web_b
    desar_juegos_b: desar_juegos_b
    desar_app_mov_b: desar_app_mov_b
    desar_sist_emb_b: desar_sist_emb_b

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
                text: "Desarrollador de Software Front End"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "[u]Otras denominaciones[/u]: Programador Front End / Analista-programador Front End / Developer Front End"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4          /2

            Label:
                text: "[u]Misión[/u]: Participar del proceso de programación / implementación teniendo como entrada las especificaciones de software y ajustándose"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4         /2       

            Label:
                text: "a tiempos y estándares de calidad y trabajo de la organización y del proyecto, ocupándose de la inerfaz gráfica para el usuario."
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4       /2                                
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4        /2          
                            
            Label:
                text: "Desarrollador de aplicaciones cliente-servidor:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: app_cs_b
                pos_hint: {"x":0.8, "top":0.75-0.125}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2
       
            Label:
                text: "Desarrollador Web:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_web_b
                pos_hint: {"x":0.8, "top":0.75-0.125*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Desarrollador de juegos / Aplicaciones lúdicas:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: desar_juegos_b
                pos_hint: {"x":0.8, "top":0.75-0.125*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2
    
            Label:
                text: "Desarrollador de Aplicaciones Móviles:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*4}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_app_mov_b
                pos_hint: {"x":0.8, "top":0.75-0.125*4}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Desarrollador de Sistemas Embebidos:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*5}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_sist_emb_b
                pos_hint: {"x":0.8, "top":0.75-0.125*5}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1) 
            on_release:            
                root.manager.transition.direction = "right" 
                root.submit()

<Perfil2c>: #Desarrollador de Software Full Stack
    name: "perfil2c"
    app_cs_c: app_cs_c
    desar_web_c: desar_web_c
    desar_juegos_c: desar_juegos_c
    desar_app_mov_c: desar_app_mov_c
    desar_sist_emb_c: desar_sist_emb_c

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
                text: "Desarrollador de Software Full Stack"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Programador Full Stack / Analista-programador Full Stack / Developer Full Stack"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4       /2

            Label:
                text: "[u]Misión[/u]: Participar del proceso de programación / implementación teniendo como entrada las especificaciones de software y ajustándose a tiempos y"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4          /2     

            Label:
                text: "estándares de calidad y trabajo de la organización y del proyecto, capaz de ocuparse tanto de la arquitectura interna como de la inerfaz gráfica para el usuario."
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4        /2                              
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4         /2         
                            
            Label:
                text: "Desarrollador de aplicaciones cliente-servidor:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12}
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: app_cs_c
                pos_hint: {"x":0.8, "top":0.75-0.125}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2
       
            Label:
                text: "Desarrollador Web:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_web_c
                pos_hint: {"x":0.8, "top":0.75-0.125*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "Desarrollador de juegos / Aplicaciones lúdicas:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4 /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: desar_juegos_c
                pos_hint: {"x":0.8, "top":0.75-0.125*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2
    
            Label:
                text: "Desarrollador de Aplicaciones Móviles:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*4}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_app_mov_c
                pos_hint: {"x":0.8, "top":0.75-0.125*4}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "Desarrollador de Sistemas Embebidos:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.12*5}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: desar_sist_emb_c
                pos_hint: {"x":0.8, "top":0.75-0.125*5}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1) 
            on_release:            
                root.manager.transition.direction = "right" 
                root.submit()

<Perfil3>: #Arquitecto de Software
    name: "perfil3"    
    app_mov: app_mov
    sist_em: sist_em

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
                text: "Arquitecto de Software"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Diseñador de Software / Diseñador de Soluciones / Desarrollador Senior"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4       /2

            Label:
                text: "[u]Misión[/u]: En cooperación con el Líder de Proyecto, participa en la toma de decisiones adecuadas para lograr una arquitectura"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4        /2     

            Label:
                text: "ajustándose a tiempos y estándares de calidad y trabajo de la organización y del proyecto"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4       /2                             
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4      /2          
                            
            Label:
                text: "Aplicaciones móviles:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: app_mov
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2
       
            Label:
                text: "Sistemas embebidos:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: sist_em
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()

<Perfil4>: #Consultor BI - Business Intelligence
    name: "perfil4"
    desar: desar
    esp_inf: esp_inf
    analist: analist

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
                text: "Consultor BI - Business Intelligence"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Analista Business Intelligence / Especialista en Business Intelligence"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4      /2   

            Label:
                text: "[u]Misión[/u]: Proveer de nuevo conocimiento relevante para la toma de decisiones en la organización"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4       /2        

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4            /2      
                            
            Label:
                text: "Desarrollador:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: desar
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4    /2
       
            Label:
                text: "Especialista en informes:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: esp_inf
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4    /2

            Label:
                text: "Analista:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: analist
                pos_hint: {"x":0.8, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4    /2
    
        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()  

<Perfil5>: #Analista de Negocios
    name: "perfil5"
    ap_erp_crm: ap_erp_crm
    esp_proc: esp_proc
    esp_ind: esp_ind

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
                text: "Analista de Negocios"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "[u]Otras denominaciones[/u]: Consultor Funcional / Analista Funcional / Analista de Procesos"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4     /2  

            Label:
                text: "[u]Misión[/u]: Acompañar los cambios y evolución de las organizaciones brindando"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4    /2         

            Label:
                text: "soluciones de valor agregado sobre sus procesos de negocios y aplicaciones"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4         /2                           
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4     /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4         /2       
                            
            Label:
                text: "Aplicaciones ERP / CRM:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4     /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: ap_erp_crm
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4    /2
       
            Label:
                text: "Especialista en procesos: financieros, logísticos, producción:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: esp_proc
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Especialista en industrias: consumo masivo, financieros, retail, etc.:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4     /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: esp_ind
                pos_hint: {"x":0.8, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()                                  

<Perfil6>: #Diseñador Web
    name: "perfil6"
    uxd: uxd
    webd: webd
    mkt: mkt

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
                text: "Diseñador Web"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "[u]Otras denominaciones[/u]: Maquetador Web / UI Developer / Front-End Designer"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4        /2 

            Label:
                text: "[u]Misión[/u]: Es quien se encarga de la identidad visual, la coherencia y consistencia gráfica del sitio web, priorizando la comunicación"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4    /2         

            Label:
                text: "y una interfaz de usuario responsiva, seleccionando los elementos que la componen y codificando los diseños en lenguajes HTML, CSS y JS"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4            /2                           
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4     /2           
                            
            Label:
                text: "UX Developer:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: uxd
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2
       
            Label:
                text: "WEBDeveloper:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: webd
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "Marketing Online:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: mkt
                pos_hint: {"x":0.8, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4 /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()                     

<Perfil7>: #Analista UI/UX (Usabilidad)
    name: "perfil7"    
    research: research
    analisis: analisis
    prot_inter: prot_inter
    test_us: test_us

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
                text: "Analista UI/UX (Usabilidad)"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Analista de Usabilidad / Analista UI/UX / Analista de Experiencia de Usuario / Consultor de Usabilidad"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4        /2

            Label:
                text: "/ Consultor UI/UX / Diseñador UI/UX / User Insight Analyst / Experience Designer / User Experience Analyst."
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4  /2

            Label:
                text: "[u]Misión[/u]: Optimizar la experiencia del usuario cuando interactúa con un software consiguiendo la mayor satisfacción y mejor experiencia de uso posible con el"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4    /2         

            Label:
                text: "mínimo esfuerzo. Lograr, utilizando técnicas de usabilidad, que un producto sea lo más eficaz, eficiente y satisfactorio para los diferentes usuarios y contextos"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.86}
                font_size: (root.width**2 + root.height**2) / 17**4      /2                              
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4    /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4        /2        
                            
            Label:
                text: "Research (en general o en técnica específica):"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: research
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2
       
            Label:
                text: "Análisis:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: analisis
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Prototipado de interfaz de usuarios:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: prot_inter
                pos_hint: {"x":0.8, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2
    
            Label:
                text: "Test de usuarios / Test de usabilidad:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*4}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: test_us
                pos_hint: {"x":0.8, "top":0.75-0.155*4}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1) 
            on_release:            
                root.manager.transition.direction = "right" 
                root.submit()

<Perfil8>: #Tester / Analista Tester
    name: "perfil8"
    orient_tec: orient_tec
    orient_func: orient_func
    orient_seg: orient_seg

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
                text: "Tester / Analista Tester"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Líder de Pruebas / Analista de Control de Calidad"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4       /2

            Label:
                text: "[u]Misión[/u]: Asegurar que el software o pieza de software funcione de acuerdo con los requisitos y trabaje con sus interfaces"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4      /2        

            Label:
                text: "de la forma esperada, detectando en forma temprana defectos y evitando propagación y llegada al cliente (interno o externo)"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4     /2                               
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4      /2           
                            
            Label:
                text: "Orientación técnica (stress, volumen, performance, etc.):"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: orient_tec
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2
       
            Label:
                text: "Orientación funcional:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: orient_func
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Orientación seguridad (técnicas de hackeo, etc.):"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: orient_seg
                pos_hint: {"x":0.8, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()

<Perfil19>: #QA Automation
    name: "perfil19"
    qa: qa

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
                text: "QA Automation"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4   /2
    
            Label:
                text: "[u]Misión[/u]: Decide cuáles de las pruebas detalladas en el plan de pruebas tiene prioridad para automatizarse."
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4   /2          

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4        /2           
                            
            Label:
                text: "QA Automation:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: qa
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil9>: #Analista de Calidad
    name: "perfil9"
    iso: iso
    itil: itil
    cmmi: cmmi

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
                text: "Analista de Calidad"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: QA / Analista de Procesos"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4      /2  

            Label:
                text: "[u]Misión[/u]: Proveer un marco de metodología y estandarización a la Organización y sus Proyectos, en dos importantes ramas:"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4      /2         

            Label:
                text: "calidad en procesos y calidad en producto, detectando en forma temprana las causas de los defectos y evitando su propagación"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4       /2                               
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4     /2           
                            
            Label:
                text: "ISO 9001 - ISO 27001:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: iso
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2
       
            Label:
                text: "Modelos de Calidad para servicios TI (ITIL / ISO 20000):"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'
                
            TextInput:
                id: itil
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "CMMI:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'               
    
            TextInput:
                id: cmmi
                pos_hint: {"x":0.8, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()

<Perfil10>: #IT Manager
    name: "perfil10"
    datcenter: datcenter
    rout_switch: rout_switch
    video: video
    voice: voice
    redes: redes
    seg: seg

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
                text: "IT Manager: Administrador de Redes, Comunicaciones y Sistemas Operativos"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Soporte de Infraestructura IT / Soporte de Redes / Especialista en Redes "
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4   /2    

            Label:
                text: "/ Técnico en Redes / Ingeniero en Redes / Administrador de Redes, Comunicaciones y Sistemas Operativos"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4     /2        

            Label:
                text: "[u]Misión[/u]: Administrar la operación, seguridad y mantenimiento de la infraestructura"
                markup: True                
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4    /2                                
                
            Label:
                text: "de redes asegurando la calidad y performance de los servicios de la Organización"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.86}
                font_size: (root.width**2 + root.height**2) / 17**4   /2

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4      /2           
                            
            Label:
                text: "Data Center:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: datcenter
                pos_hint: {"x":0.4, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Routing and Switching:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'

            TextInput:
                id: rout_switch
                pos_hint: {"x":0.4, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

            Label:
                text: "Video:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15*3}
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'    

            TextInput:
                id: video
                pos_hint: {"x":0.4, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "Voice:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.55, "top":0.75-0.15}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'

            TextInput:
                id: voice
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2
        
            Label:
                text: "Redes Wireless:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.55, "top":0.75-0.15*2}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'

            TextInput:
                id: redes
                pos_hint: {"x":0.8, "top":0.75-0.155*2}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "Seguridad:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.55, "top":0.75-0.15*3}                
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'

            TextInput:
                id: seg
                pos_hint: {"x":0.8, "top":0.75-0.155*3}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2
                
        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1) 
            on_release:            
                root.manager.transition.direction = "right" 
                root.submit()

<Perfil11>: #Administrador de Base de Datos (DBA)
    name: "perfil11"
    dba: dba

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
                text: "Administrador de Base de Datos (DBA)"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Analista de Bases de Datos / DBA (Database Administrator)"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4      /2   

            Label:
                text: "[u]Misión[/u]: Garantizar y optimizar la seguridad, integridad y estabilidad de las bases de datos que"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4      /2         

            Label:
                text: "administran la información de las operaciones del negocio, para que siempre estén disponibles con tiempos de respuesta óptimos,"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4   /2

            Label:
                text: " según las diferentes áreas de la compañía. En términos tecnológicos: asegurar la continuidad operacional"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.86}
                font_size: (root.width**2 + root.height**2) / 17**4      /2                                            
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4       /2         
                            
            Label:
                text: "Administrador de Base de Datos (DBA):"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4    /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: dba
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil12>: #Analista funcional
    name: "perfil12"
    afunc: afunc

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
                text: "Analista Funcional"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Analista de Sistemas / Analista Técnico Funcional / Business Partner"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4        /2 

            Label:
                text: "[u]Misión[/u]: Establecer los requisitos funcionales del sistema"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4       /2                                                      
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4        /2         
                            
            Label:
                text: "Analista Funcional:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: afunc
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil13>: #Analista Big Data - Data Scientist
    name: "perfil13"
    dscience: dscience

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
                text: "Analista Big Data - Data Scientist"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Experto en Big Data / Analista Data Scientist / 'Chief data officer' (CDO) / Analista Digital"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4      /2   

            Label:
                text: "[u]Misión[/u]: Responsable de los datos empresariales y de la estrategia de la información. Debe diseñar, implantar y optimizar una estrategia"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4        /2       

            Label:
                text: " a largo plazo del manejo de la información en la empresa. Es el encargado de analizar datos cuantitativos y cualitativos del entorno digital para"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4   /2

            Label:
                text: "extraer información de valor que ayude a tomar decisiones"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.86}
                font_size: (root.width**2 + root.height**2) / 17**4      /2                                            
                
            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4       /2         
                            
            Label:
                text: "Analista Big Data - Data Scientist:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: dscience
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil14>: #Analista Middleware
    name: "perfil14"
    midd: midd

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
                text: "Analista Middleware"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4 /2

            Label:
                text: "[u]Otras denominaciones[/u]: Administrador de Middleware / Ingeniero en Soporte Middleware / Ingeniero Middleware / Consultor Middleware"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4     /2  

            Label:
                text: "[u]Misión[/u]: Es el responsable de la administración de aplicaciones Middleware (programas que asisten a una aplicación para interactuar"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4     /2        

            Label:
                text: "o comunicarse con otras aplicaciones, o paquetes de programas, redes, hardware y/o sistemas operativos)"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4   /2

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4      /2          
                            
            Label:
                text: "Analista Middleware:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: midd
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil15>: #Soporte Técnico
    name: "perfil15"
    soporte: soporte

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
                text: "Soporte Técnico"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Technical Support Engineer / Global Support Engineer / Atención al Usuario / Customer Care"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4       /2 

            Label:
                text: "[u]Misión[/u]: Asistir al usuario en las dudas sobre el uso o resolución de problemas de la aplicación una vez que esta haya pasado la etapa de desarrollo"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4     /2         

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4     /2           
                            
            Label:
                text: "Soporte Técnico:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4  /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: soporte
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4 /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil16>: #Especialista en Seguridad de la Información
    name: "perfil16"
    esp_seg: esp_seg

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
                text: "Especialista en Seguridad de la Información"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Analista de Seguridad / Especialista en Seguridad Informática"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4       /2  

            Label:
                text: "[u]Misión[/u]: Proveer un marco de metodología y estandarización de seguridad de información a la organización y sus proyectos,"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4      /2       

            Label:
                text: "detectando en forma temprana causas de desvíos, implementando y administrando sistemas, políticas y normatividad de seguridad informática"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4   /2

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4       /2           
                            
            Label:
                text: "Especialista en Seguridad de la Información:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: esp_seg
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil17>: #Implementador Configuration Manager
    name: "perfil17"
    config: config

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
                text: "Implementador Configuration Manager"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Configuration Manager / Release Manager / Implementation Manager / Implementador de Despliegues"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4      /2   

            Label:
                text: "[u]Misión[/u]: Mantenimiento de la integridad de la configuración a lo largo del ciclo de vida de los componentes de software,"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4       /2      

            Label:
                text: "mediante actividades de planificación, despliegue, control y auditoría"
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4     /2

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4          /2        
                            
            Label:
                text: "Implementador Configuration Manager:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: config
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4   /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil18>: #Implementador Software de Gestión
    name: "perfil18"
    soft_gest: soft_gest

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
                text: "Implementador Software de Gestión"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Analista Técnico"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4       /2  

            Label:
                text: "[u]Misión[/u]: Diseñar e implementar la parametrización requerida para reflejar las particularidades de cada proyecto"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4       /2        

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4        /2         
                            
            Label:
                text: "Implementador Software de Gestión:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: soft_gest
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil20>: #DevOps
    name: "perfil20"
    devops: devops

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
                text: "DevOps"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: Site Reliability Engineer / Devops Consultant"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4        /2                 
    
            Label:
                text: "[u]Misión[/u]: Transformar culturalmente el área de development. Hacer que todo"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4       /2        

            Label:
                text: "el ciclo de vida de la aplicación sea mejor y tenga menores errores cuando llegue a producción."
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4   /2

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4  /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4          /2      
                            
            Label:
                text: "DevOps:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: devops
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4  /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit() 

<Perfil21>: #Experto en Machine Learning
    name: "perfil21"
    malearn: malearn

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
                text: "Experto en Machine Learning"
                #color: (0/255 ,0/255, 0/255,1)
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":1}
                font_size: (root.width**2 + root.height**2) / 14**4  /2

            Label:
                text: "[u]Otras denominaciones[/u]: - "
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.95}
                font_size: (root.width**2 + root.height**2) / 17**4     /2                  
    
            Label:
                text: "[u]Misión[/u]: Diseño de software de ejecución automática para automatizar modelos predictivos,"
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.92}
                font_size: (root.width**2 + root.height**2) / 17**4      /2       

            Label:
                text: "incluyendo modelos de árboles de decisión, random forest, redes neuronales, entre otros."
                markup: True
                size_hint: 0.8, 0.2
                pos_hint: {"x":0.1, "top":0.89}
                font_size: (root.width**2 + root.height**2) / 17**4   /2

            Label:
                text: "Indique, para cada especialidad, la cantidad de búsquedas activas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.75}
                font_size: (root.width**2 + root.height**2) / 14.5**4   /2

            Label:
                text: "Puede dejar en blanco las especialidades sin búsquedas actuales"
                size_hint: 0.4,0.1
                pos_hint: {"x":0.3, "top":0.7}
                font_size: (root.width**2 + root.height**2) / 17**4        /2         
                            
            Label:
                text: "Experto en Machine Learning:"
                size_hint: 0.4,0.08
                pos_hint: {"x":0.1, "top":0.75-0.15}
                font_size: (root.width**2 + root.height**2) / 15.5**4   /2
                text_size: self.size
                halign: 'left'                
    
            TextInput:
                id: malearn
                pos_hint: {"x":0.8, "top":0.75-0.155}
                size_hint: 0.12, 0.09
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4   /2

        Button:
            pos_hint:{"x":0.2,"y":0.05}
            size_hint: 0.6, 0.15
            text: "Ingresar valores y volver al menú anterior"
            font_size: (root.width**2 + root.height**2) / 14**4  /2
            on_press: 
                self.background_color = (0/255,51/255,102/255,1)   
            on_release:
                root.manager.transition.direction = "right"            
                root.submit()                
""") 

#lista para chequear que se ingresen valores númericos en los inputs de la app
x = range(9999)
y = []
for n in x:
    y.append(str(n))


#path = os.getcwd()        #comando para Windows
path = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])  #comando para mac
files = os.listdir(path)

for i in range(0,len(files)):
    if files[i].endswith('.xlsx'):
        urls = pd.read_excel(path+'/'+files[i])

class Introduccion(Screen):
    def perfil_csv(self):
    #Creamos .csv de perfiles
        #perfil 1a
        data1 = {'x1_11':([0]*len(urls)), 'x1_12':([0]*len(urls)), 'x1_13':([0]*len(urls))}
        df_data1 = pd.DataFrame.from_dict(data1)
        df_data1.to_csv("perfil1.csv")
        #perfil 1b Cloud Engineer
        data1b = {'x1b_11':([0]*len(urls))}
        df_data1b = pd.DataFrame.from_dict(data1b)
        df_data1b.to_csv("perfil1b.csv")        
        #perfil 2a
        data2 = {'x2_11':([0]*len(urls)), 'x2_12':([0]*len(urls)), 'x2_13':([0]*len(urls)), 'x2_14':([0]*len(urls)), 'x2_15':([0]*len(urls))}
        df_data2 = pd.DataFrame.from_dict(data2)
        df_data2.to_csv("perfil2.csv")
        #perfil 2b
        data2b = {'x2b_11':([0]*len(urls)), 'x2b_12':([0]*len(urls)), 'x2b_13':([0]*len(urls)), 'x2b_14':([0]*len(urls)), 'x2b_15':([0]*len(urls))}
        df_data2b = pd.DataFrame.from_dict(data2b)
        df_data2b.to_csv("perfil2b.csv")
        #perfil 2c
        data2c = {'x2c_11':([0]*len(urls)), 'x2c_12':([0]*len(urls)), 'x2c_13':([0]*len(urls)), 'x2c_14':([0]*len(urls)), 'x2c_15':([0]*len(urls))}
        df_data2c = pd.DataFrame.from_dict(data2c)
        df_data2c.to_csv("perfil2c.csv")
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
        #perfil19
        data19 = {'x19_11':([0]*len(urls))}
        df_data19 = pd.DataFrame.from_dict(data19)
        df_data19.to_csv("perfil19.csv") 
        #perfil20
        data20 = {'x20_11':([0]*len(urls))}
        df_data20 = pd.DataFrame.from_dict(data20)
        df_data20.to_csv("perfil20.csv")  
        #perfil21
        data21 = {'x21_11':([0]*len(urls))}
        df_data21 = pd.DataFrame.from_dict(data21)
        df_data21.to_csv("perfil21.csv")               

class MainWindow(Screen):
    def btn(self):
        mensaje_final()

class Popups(FloatLayout):
    def fin(self):
        p1 = pd.read_csv('perfil1.csv')
        p1b = pd.read_csv('perfil1b.csv') #respuestas a la primera pregunta
        p2a = pd.read_csv('perfil2.csv') #respuestas a la segunda pregunta
        p2b = pd.read_csv('perfil2b.csv')
        p2c = pd.read_csv('perfil2c.csv')
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
        p19 = pd.read_csv('perfil19.csv') #respuestas a la segunda pregunta
        p20 = pd.read_csv('perfil20.csv') #respuestas a la segunda pregunta  
        p21 = pd.read_csv('perfil21.csv')   

        #path = os.getcwd()        #comando para Windows
        path = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])  #comando para mac
        files = os.listdir(path)

        for i in range(0,len(files)):
            if files[i].endswith('.xlsx'):
                urls = pd.read_excel(path+'/'+files[i])

        urls = urls.links.sample(frac = 1).reset_index(drop=True) #orden aleatorio de links
        urls = urls.to_frame() 
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_window_position(-10000,0) # escondemos el web driver
        
        #loopeamos por la cantidad de respuestas en el df
        for user_id in range(len(urls)):
            driver.get(urls.links[user_id])
            driver = answers(driver = driver, df = p1, rta1 = rta1, rta2 = rta2, rta3 = rta3, user_id = user_id)
            driver = answers1b(driver = driver, df = p1b, rta1ba = rta1b_a, user_id = user_id)
            driver = answers2(driver = driver, df = p2a, rta2a = rta2_a, rta2b = rta2_b,
                        rta2c = rta2_c, rta2d = rta2_d, rta2e = rta2_e, user_id = user_id)
            driver = answers2b(driver = driver, df = p2b, rta2ba = rta2b_a, rta2bb = rta2b_b,
                        rta2bc = rta2b_c, rta2bd = rta2b_d, rta2be = rta2b_e, user_id = user_id)
            driver = answers2c(driver = driver, df = p2c, rta2ca = rta2c_a, rta2cb = rta2c_b,
                        rta2cc = rta2c_c, rta2cd = rta2c_d, rta2ce = rta2c_e, user_id = user_id)                        
            driver = answers3(driver = driver, df = p3, rta3a = rta3_a, rta3b = rta3_b, user_id = user_id)
            driver = answers4(driver = driver, df = p4, rta4a = rta4_a, rta4b = rta4_b, rta4c = rta4_c, user_id = user_id)
            driver = answers5(driver = driver, df = p5, rta5a = rta5_a, rta5b = rta5_b, rta5c = rta5_c, user_id = user_id)
            driver = answers6(driver = driver, df = p6, rta6a = rta6_a, rta6b = rta6_b, rta6c = rta6_c, user_id = user_id)
            driver = answers7(driver = driver, df = p7, rta7a = rta7_a, rta7b = rta7_b,
                        rta7c = rta7_c, rta7d = rta7_d, user_id = user_id)
            driver = answers8(driver = driver, df = p8, rta8a = rta8_a, rta8b = rta8_b, rta8c = rta8_c, user_id = user_id)
            driver = answers19(driver = driver, df = p19, rta19a = rta19_a, user_id = user_id)
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
            driver = answers20(driver = driver, df = p20, rta20a = rta20_a, user_id = user_id)
            driver = answers21(driver = driver, df = p21, rta21a = rta21_a, user_id = user_id)
            driver = submit(driver = driver, element_class = submit_class)            

        driver.close() # cerramos el web driver
        perfiles = ["perfil1.csv", "perfil1b.csv", "perfil2.csv", "perfil2b.csv", "perfil2c.csv", "perfil3.csv", "perfil4.csv", "perfil5.csv",
                    "perfil6.csv", "perfil7.csv", "perfil8.csv", "perfil9.csv", "perfil10.csv", "perfil11.csv", "perfil12.csv",
                    "perfil13.csv", "perfil14.csv", "perfil15.csv", "perfil16.csv", "perfil17.csv", "perfil18.csv", "perfil19.csv",
                    "perfil20.csv", "perfil21.csv"]
        for perfil in perfiles:
            os.remove(perfil)

        FormularioTECx.get_running_app().stop()
       
class Perfil1(Screen): #Líder de Desarrollo / Project Manager (PM)
    pm = ObjectProperty(None)
    sdm = ObjectProperty(None)
    scr = ObjectProperty(None)
    
    def submit(self):
        if ((self.pm.text in y or self.pm.text.count("") == 1) and (self.sdm.text in y or self.sdm.text.count("") == 1)
        and (self.scr.text in y or self.scr.text.count("") == 1)):
            x1_11 = fragmentar(self.pm.text)
            x1_12 = fragmentar(self.sdm.text)
            x1_13 = fragmentar(self.scr.text)
        
            sm.current = "main"        
          
            perfil1_dict = {'x1_11':x1_11, 'x1_12':x1_12, 'x1_13':x1_13}
            df_perfil1 = pd.DataFrame.from_dict(perfil1_dict)
            df_perfil1.to_csv("perfil1.csv")

        else:
            invalidForm()
            sm.current = "perfil1"
            self.reset()
    def reset(self):
        self.pm.text = ""
        self.sdm.text = ""
        self.scr.text = ""     

class Perfil1b(Screen): #Cloud Engineer
    ceng = ObjectProperty(None)

    def submit(self):
        if ((self.ceng.text in y or self.ceng.text.count("") == 1)):
            x1b_11 = fragmentar(self.ceng.text)
        
            sm.current = "main"        
          
            perfil1b_dict = {'x1b_11':x1b_11}
            df_perfil1b= pd.DataFrame.from_dict(perfil1b_dict)
            df_perfil1b.to_csv("perfil1b.csv")

        else:
            invalidForm()
            sm.current = "perfil1b"
            self.reset() 
    def reset(self):
        self.ceng.text = ""

class Perfil2a(Screen): #Desarrollador de Software Back End
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
            sm.current = "perfil2a"
            self.reset() 
    def reset(self):
        self.app_cs.text = ""
        self.desar_web.text = ""
        self.desar_juegos.text = ""
        self.desar_app_mov.text = ""  
        self.desar_sist_emb.text = ""          

class Perfil2b(Screen): #Desarrollador de Software Front End
    app_cs_b = ObjectProperty(None)
    desar_web_b = ObjectProperty(None)
    desar_juegos_b = ObjectProperty(None)
    desar_app_mov_b = ObjectProperty(None)
    desar_sist_emb_b = ObjectProperty(None)

    def submit(self):
        if ((self.app_cs_b.text in y or self.app_cs_b.text.count("") == 1) and (self.desar_web_b.text in y or self.desar_web_b.text.count("") == 1)
                and (self.desar_juegos_b.text in y or self.desar_juegos_b.text.count("") == 1) and (self.desar_app_mov_b.text in y or self.desar_app_mov_b.text.count("") == 1)
                and (self.desar_sist_emb_b.text in y or self.desar_sist_emb_b.text.count("") == 1)):
            x2b_11 = fragmentar(self.app_cs_b.text)
            x2b_12 = fragmentar(self.desar_web_b.text)
            x2b_13 = fragmentar(self.desar_juegos_b.text)
            x2b_14 = fragmentar(self.desar_app_mov_b.text)
            x2b_15 = fragmentar(self.desar_sist_emb_b.text)
            sm.current = "main"
            
            perfil2b_dict = {'x2b_11':x2b_11, 'x2b_12':x2b_12, 'x2b_13':x2b_13, 'x2b_14':x2b_14, 'x2b_15':x2b_15}
            df_perfil2b = pd.DataFrame.from_dict(perfil2b_dict)
            df_perfil2b.to_csv("perfil2b.csv")

        else:
            invalidForm()
            sm.current = "perfil2b"
            self.reset() 
    def reset(self):
        self.app_cs_b.text = ""
        self.desar_web_b.text = ""
        self.desar_juegos_b.text = ""
        self.desar_app_mov_b.text = ""  
        self.desar_sist_emb_b.text = ""  

class Perfil2c(Screen): #Desarrollador de Software Full Stack
    app_cs_c = ObjectProperty(None)
    desar_web_c = ObjectProperty(None)
    desar_juegos_c = ObjectProperty(None)
    desar_app_mov_c = ObjectProperty(None)
    desar_sist_emb_c = ObjectProperty(None)

    def submit(self):
        if ((self.app_cs_c.text in y or self.app_cs_c.text.count("") == 1) and (self.desar_web_c.text in y or self.desar_web_c.text.count("") == 1)
                and (self.desar_juegos_c.text in y or self.desar_juegos_c.text.count("") == 1) and (self.desar_app_mov_c.text in y or self.desar_app_mov_c.text.count("") == 1)
                and (self.desar_sist_emb_c.text in y or self.desar_sist_emb_c.text.count("") == 1)):
            x2c_11 = fragmentar(self.app_cs_c.text)
            x2c_12 = fragmentar(self.desar_web_c.text)
            x2c_13 = fragmentar(self.desar_juegos_c.text)
            x2c_14 = fragmentar(self.desar_app_mov_c.text)
            x2c_15 = fragmentar(self.desar_sist_emb_c.text)
            sm.current = "main"
            
            perfil2c_dict = {'x2c_11':x2c_11, 'x2c_12':x2c_12, 'x2c_13':x2c_13, 'x2c_14':x2c_14, 'x2c_15':x2c_15}
            df_perfil2c = pd.DataFrame.from_dict(perfil2c_dict)
            df_perfil2c.to_csv("perfil2c.csv")

        else:
            invalidForm()
            sm.current = "perfil2c"
            self.reset() 
    def reset(self):
        self.app_cs_c.text = ""
        self.desar_web_c.text = ""
        self.desar_juegos_c.text = ""
        self.desar_app_mov_c.text = ""  
        self.desar_sist_emb_c.text = ""  

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

class Perfil7(Screen): #Analista UI/UX (Usabilidad)
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

class Perfil19(Screen): #QA Automation
    qa = ObjectProperty(None)

    def submit(self):
        if ((self.qa.text in y or self.qa.text.count("") == 1)):
            x19_11 = fragmentar(self.qa.text)
        
            sm.current = "main"        
          
            perfil19_dict = {'x19_11':x19_11}
            df_perfil19= pd.DataFrame.from_dict(perfil19_dict)
            df_perfil19.to_csv("perfil19.csv")

        else:
            invalidForm()
            sm.current = "perfil19"
            self.reset() 
    def reset(self):
        self.qa.text = ""        

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

class Perfil21(Screen): #Experto en Machine Learning
    malearn = ObjectProperty(None)

    def submit(self):
        if ((self.malearn.text in y or self.malearn.text.count("") == 1)):
            x21_11 = fragmentar(self.malearn.text)
        
            sm.current = "main"        
          
            perfil21_dict = {'x21_11':x21_11}
            df_perfil21= pd.DataFrame.from_dict(perfil21_dict)
            df_perfil21.to_csv("perfil21.csv")

        else:
            invalidForm()
            sm.current = "perfil21"
            self.reset() 
    def reset(self):
        self.malearn.text = ""

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

class Perfil20(Screen): #DevOps
    devops = ObjectProperty(None)

    def submit(self):
        if ((self.devops.text in y or self.devops.text.count("") == 1)):
            x20_11 = fragmentar(self.devops.text)
        
            sm.current = "main"        
          
            perfil20_dict = {'x20_11':x20_11}
            df_perfil20= pd.DataFrame.from_dict(perfil20_dict)
            df_perfil20.to_csv("perfil20.csv")

        else:
            invalidForm()
            sm.current = "perfil20"
            self.reset() 
    def reset(self):
        self.devops.text = ""

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
        size_hint=(None, None), size=(800, 600))   

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

#kv = Builder.load_file("KvEstructura.kv") #cargamos la estructura del app

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("TECx.png")
#para el web scraping
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from parsel import Selector
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# url = "https://economictrends.limequery.com/214733?token=1234&lang=es"
# driver = webdriver.Chrome(ChromeDriverManager().install())

#P1 Líder de Desarrollo / Proyect Manager (PM)
rta1 = 'answer661992X506X16497SQ001_SQ001'
rta2 = 'answer661992X506X16497SQ002_SQ001'
rta3 = 'answer661992X506X16497SQ003_SQ001'
def answers(driver, df, rta1, rta2, rta3, user_id):     
    #definimos las posibles respuestas a la pregunta
    x1_11 = df["x1_11"][user_id] #busqueda activa
    x1_12 = df["x1_12"][user_id] #busqueda activa
    x1_13 = df["x1_13"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x1_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta1)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x1_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta2)
    text_questions2.send_keys(text_answers2)

    #ingresamos los valores
    text_answers3 = str(x1_13) #send keys funciona con str, pero llegan al formulario como int
    text_questions3 = driver.find_element(By.ID,rta3)
    text_questions3.send_keys(text_answers3)    

    return driver

#P1 Cloud Engineer
rta1b_a = 'answer661992X506X16580'
def answers1b(driver, df, rta1ba, user_id):     
    #definimos las posibles respuestas a la pregunta
    x1b_11 = df["x1b_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x1b_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta1ba)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P2 Desarrollador de Software Back End
rta2_a = 'answer661992X506X16563SQ001_SQ001'
rta2_b = 'answer661992X506X16563SQ002_SQ001'
rta2_c = 'answer661992X506X16563SQ003_SQ001'
rta2_d = 'answer661992X506X16563SQ004_SQ001'
rta2_e = 'answer661992X506X16563SQ005_SQ001'
def answers2(driver, df, rta2a, rta2b, rta2c, rta2d, rta2e, user_id):
    x2_11 = df["x2_11"][user_id] #busqueda activa
    x2_12 = df["x2_12"][user_id] #busqueda activa
    x2_13 = df["x2_13"][user_id] #busqueda activa
    x2_14 = df["x2_14"][user_id] #busqueda activa
    x2_15 = df["x2_15"][user_id] #busqueda activa
    
    text_answers1 = str(x2_11) # following the order in the form
    text_questions1 = driver.find_element(By.ID,rta2a)
    text_questions1.send_keys(text_answers1)        
        
    text_answers2 = str(x2_12) # following the order in the form
    text_questions2 = driver.find_element(By.ID,rta2b)
    text_questions2.send_keys(text_answers2)     
    
    text_answers3 = str(x2_13) # following the order in the form
    text_questions3 = driver.find_element(By.ID,rta2c)
    text_questions3.send_keys(text_answers3)        
        
    text_answers4 = str(x2_14) # following the order in the form
    text_questions4 = driver.find_element(By.ID,rta2d)
    text_questions4.send_keys(text_answers4)      

    text_answers5 = str(x2_15) # following the order in the form
    text_questions5 = driver.find_element(By.ID,rta2e)
    text_questions5.send_keys(text_answers5)  
    
    return driver

#P2 Desarrollador de Software Front End
rta2b_a = 'answer661992X506X16570SQ001_SQ001'
rta2b_b = 'answer661992X506X16570SQ002_SQ001'
rta2b_c = 'answer661992X506X16570SQ003_SQ001'
rta2b_d = 'answer661992X506X16570SQ004_SQ001'
rta2b_e = 'answer661992X506X16570SQ005_SQ001'
def answers2b(driver, df, rta2ba, rta2bb, rta2bc, rta2bd, rta2be, user_id):
    x2b_11 = df["x2b_11"][user_id] #busqueda activa
    x2b_12 = df["x2b_12"][user_id] #busqueda activa
    x2b_13 = df["x2b_13"][user_id] #busqueda activa
    x2b_14 = df["x2b_14"][user_id] #busqueda activa
    x2b_15 = df["x2b_15"][user_id] #busqueda activa
    
    text_answers1 = str(x2b_11) # following the order in the form
    text_questions1 = driver.find_element(By.ID,rta2ba)
    text_questions1.send_keys(text_answers1)        
        
    text_answers2 = str(x2b_12) # following the order in the form
    text_questions2 = driver.find_element(By.ID,rta2bb)
    text_questions2.send_keys(text_answers2)     
    
    text_answers3 = str(x2b_13) # following the order in the form
    text_questions3 = driver.find_element(By.ID,rta2bc)
    text_questions3.send_keys(text_answers3)        
        
    text_answers4 = str(x2b_14) # following the order in the form
    text_questions4 = driver.find_element(By.ID,rta2bd)
    text_questions4.send_keys(text_answers4)      

    text_answers5 = str(x2b_15) # following the order in the form
    text_questions5 = driver.find_element(By.ID,rta2be)
    text_questions5.send_keys(text_answers5)  
    
    return driver

#P2 Desarrollador de Software Full Stack
rta2c_a = 'answer661992X506X16507SQ001_SQ001'
rta2c_b = 'answer661992X506X16507SQ002_SQ001'
rta2c_c = 'answer661992X506X16507SQ003_SQ001'
rta2c_d = 'answer661992X506X16507SQ004_SQ001'
rta2c_e = 'answer661992X506X16507SQ005_SQ001'
def answers2c(driver, df, rta2ca, rta2cb, rta2cc, rta2cd, rta2ce, user_id):
    x2c_11 = df["x2c_11"][user_id] #busqueda activa
    x2c_12 = df["x2c_12"][user_id] #busqueda activa
    x2c_13 = df["x2c_13"][user_id] #busqueda activa
    x2c_14 = df["x2c_14"][user_id] #busqueda activa
    x2c_15 = df["x2c_15"][user_id] #busqueda activa
    
    text_answers1 = str(x2c_11) # following the order in the form
    text_questions1 = driver.find_element(By.ID,rta2ca)
    text_questions1.send_keys(text_answers1)        
        
    text_answers2 = str(x2c_12) # following the order in the form
    text_questions2 = driver.find_element(By.ID,rta2cb)
    text_questions2.send_keys(text_answers2)     
    
    text_answers3 = str(x2c_13) # following the order in the form
    text_questions3 = driver.find_element(By.ID,rta2cc)
    text_questions3.send_keys(text_answers3)        
        
    text_answers4 = str(x2c_14) # following the order in the form
    text_questions4 = driver.find_element(By.ID,rta2cd)
    text_questions4.send_keys(text_answers4)      

    text_answers5 = str(x2c_15) # following the order in the form
    text_questions5 = driver.find_element(By.ID,rta2ce)
    text_questions5.send_keys(text_answers5)  
    
    return driver        

#P3 Arquitecto de Software
rta3_a = 'answer661992X506X16505SQ001_SQ001'
rta3_b = 'answer661992X506X16505SQ002_SQ001'
def answers3(driver, df, rta3a, rta3b, user_id):
    #definimos las posibles respuestas a la pregunta
    x3_11 = df["x3_11"][user_id] #busqueda activa
    x3_12 = df["x3_12"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x3_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta3a)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x3_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta3b)
    text_questions2.send_keys(text_answers2)     
    
    return driver

#P4 Consultor BI - Business Intelligence
rta4_a = 'answer661992X506X16506SQ001_SQ001'
rta4_b = 'answer661992X506X16506SQ002_SQ001'
rta4_c = 'answer661992X506X16506SQ003_SQ001'
def answers4(driver, df, rta4a, rta4b, rta4c, user_id):
    #definimos las posibles respuestas a la pregunta
    x4_11 = df["x4_11"][user_id] #busqueda activa
    x4_12 = df["x4_12"][user_id] #busqueda activa
    x4_13 = df["x4_13"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x4_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta4a)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x4_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta4b)
    text_questions2.send_keys(text_answers2)     

    #ingresamos los valores
    text_answers3 = str(x4_13) #send keys funciona con str, pero llegan al formulario como int
    text_questions3 = driver.find_element(By.ID,rta4c)
    text_questions3.send_keys(text_answers3)     
        
    return driver

#P5 Analista de Negocios
rta5_a = 'answer661992X506X16501SQ001_SQ001'
rta5_b = 'answer661992X506X16501SQ002_SQ001'
rta5_c = 'answer661992X506X16501SQ003_SQ001'
def answers5(driver, df, rta5a, rta5b, rta5c, user_id):
    #definimos las posibles respuestas a la pregunta
    x5_11 = df["x5_11"][user_id] #busqueda activa
    x5_12 = df["x5_12"][user_id] #busqueda activa
    x5_13 = df["x5_13"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x5_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta5a)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x5_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta5b)
    text_questions2.send_keys(text_answers2)     

    #ingresamos los valores
    text_answers3 = str(x5_13) #send keys funciona con str, pero llegan al formulario como int
    text_questions3 = driver.find_element(By.ID,rta5c)
    text_questions3.send_keys(text_answers3)     
        
    return driver

#P6 Diseñador Web
rta6_a = 'answer661992X506X16508SQ001_SQ001'
rta6_b = 'answer661992X506X16508SQ002_SQ001'
rta6_c = 'answer661992X506X16508SQ003_SQ001'
def answers6(driver, df, rta6a, rta6b, rta6c, user_id):
    #definimos las posibles respuestas a la pregunta
    x6_11 = df["x6_11"][user_id] #busqueda activa
    x6_12 = df["x6_12"][user_id] #busqueda activa
    x6_13 = df["x6_13"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x6_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta6a)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x6_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta6b)
    text_questions2.send_keys(text_answers2)     

    #ingresamos los valores
    text_answers3 = str(x6_13) #send keys funciona con str, pero llegan al formulario como int
    text_questions3 = driver.find_element(By.ID,rta6c)
    text_questions3.send_keys(text_answers3)     
        
    return driver

#P7 Analista UX (Usabilidad)
rta7_a = 'answer661992X506X16504SQ001_SQ001'
rta7_b = 'answer661992X506X16504SQ002_SQ001'
rta7_c = 'answer661992X506X16504SQ003_SQ001'
rta7_d = 'answer661992X506X16504SQ004_SQ001'
def answers7(driver, df, rta7a, rta7b, rta7c, rta7d, user_id):
    x7_11 = df["x7_11"][user_id] #busqueda activa
    x7_12 = df["x7_12"][user_id] #busqueda activa
    x7_13 = df["x7_13"][user_id] #busqueda activa
    x7_14 = df["x7_14"][user_id] #busqueda activa
    
    
    text_answers1 = str(x7_11) # following the order in the form
    text_questions1 = driver.find_element(By.ID,rta7a)
    text_questions1.send_keys(text_answers1)        
        
    text_answers2 = str(x7_12) # following the order in the form
    text_questions2 = driver.find_element(By.ID,rta7b)
    text_questions2.send_keys(text_answers2)     
    
    text_answers3 = str(x7_13) # following the order in the form
    text_questions3 = driver.find_element(By.ID,rta7c)
    text_questions3.send_keys(text_answers3)        
        
    text_answers4 = str(x7_14) # following the order in the form
    text_questions4 = driver.find_element(By.ID,rta7d)
    text_questions4.send_keys(text_answers4)        
    
    return driver

#P8 Tester / Analista Tester
rta8_a = 'answer661992X506X16514SQ001_SQ001'
rta8_b = 'answer661992X506X16514SQ002_SQ001'
rta8_c = 'answer661992X506X16514SQ003_SQ001'
def answers8(driver, df, rta8a, rta8b, rta8c, user_id):
    #definimos las posibles respuestas a la pregunta
    x8_11 = df["x8_11"][user_id] #busqueda activa
    x8_12 = df["x8_12"][user_id] #busqueda activa
    x8_13 = df["x8_13"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x8_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta8a)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x8_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta8b)
    text_questions2.send_keys(text_answers2)     

    #ingresamos los valores
    text_answers3 = str(x8_13) #send keys funciona con str, pero llegan al formulario como int
    text_questions3 = driver.find_element(By.ID,rta8c)
    text_questions3.send_keys(text_answers3)     
        
    return driver

#P9 Analista de Calidad
rta9_a = 'answer661992X506X16500SQ001_SQ001'
rta9_b = 'answer661992X506X16500SQ002_SQ001'
rta9_c = 'answer661992X506X16500SQ003_SQ001'
def answers9(driver, df, rta9a, rta9b, rta9c, user_id):
    #definimos las posibles respuestas a la pregunta
    x9_11 = df["x9_11"][user_id] #busqueda activa
    x9_12 = df["x9_12"][user_id] #busqueda activa
    x9_13 = df["x9_13"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x9_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta9a)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x9_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta9b)
    text_questions2.send_keys(text_answers2)     

    #ingresamos los valores
    text_answers3 = str(x9_13) #send keys funciona con str, pero llegan al formulario como int
    text_questions3 = driver.find_element(By.ID,rta9c)
    text_questions3.send_keys(text_answers3)     
        
    return driver

#P10 IT Manager
rta10_a = 'answer661992X506X16512SQ001_SQ001'
rta10_b = 'answer661992X506X16512SQ002_SQ001'
rta10_c = 'answer661992X506X16512SQ003_SQ001'
rta10_d = 'answer661992X506X16512SQ004_SQ001'
rta10_e = 'answer661992X506X16512SQ005_SQ001'
rta10_f = 'answer661992X506X16512SQ006_SQ001'
def answers10(driver, df, rta10a, rta10b, rta10c, rta10d, rta10e, rta10f, user_id):
    #definimos las posibles respuestas a la pregunta
    x10_11 = df["x10_11"][user_id] #busqueda activa
    x10_12 = df["x10_12"][user_id] #busqueda activa
    x10_13 = df["x10_13"][user_id] #busqueda activa
    x10_14 = df["x10_14"][user_id] #busqueda activa
    x10_15 = df["x10_15"][user_id] #busqueda activa
    x10_16 = df["x10_16"][user_id] #busqueda activa

    #ingresamos los valores
    text_answers1 = str(x10_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta10a)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x10_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta10b)
    text_questions2.send_keys(text_answers2)     

    #ingresamos los valores
    text_answers3 = str(x10_13) #send keys funciona con str, pero llegan al formulario como int
    text_questions3 = driver.find_element(By.ID,rta10c)
    text_questions3.send_keys(text_answers3)

    #ingresamos los valores
    text_answers4 = str(x10_14) #send keys funciona con str, pero llegan al formulario como int
    text_questions4 = driver.find_element(By.ID,rta10d)
    text_questions4.send_keys(text_answers4)

    #ingresamos los valores
    text_answers5 = str(x10_15) #send keys funciona con str, pero llegan al formulario como int
    text_questions5 = driver.find_element(By.ID,rta10e)
    text_questions5.send_keys(text_answers5)

    #ingresamos los valores
    text_answers6 = str(x10_16) #send keys funciona con str, pero llegan al formulario como int
    text_questions6 = driver.find_element(By.ID,rta10f)
    text_questions6.send_keys(text_answers6)                 
        
    return driver

#P11 Administrador de Base de Datos (DBA)
rta11_a = 'answer661992X506X16498'
def answers11(driver, df, rta11a, user_id):
    #definimos las posibles respuestas a la pregunta
    x11_11 = df["x11_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x11_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta11a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P12 Analista Funcional
rta12_a = 'answer661992X506X16502'
def answers12(driver, df, rta12a, user_id):
    #definimos las posibles respuestas a la pregunta
    x12_11 = df["x12_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x12_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta12a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P13 Analista Big Data - Data Scientist
rta13_a = 'answer661992X506X16499'
def answers13(driver, df, rta13a, user_id):
    #definimos las posibles respuestas a la pregunta
    x13_11 = df["x13_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x13_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta13a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P14 Analista Middleware
rta14_a = 'answer661992X506X16503'
def answers14(driver, df, rta14a, user_id):
    #definimos las posibles respuestas a la pregunta
    x14_11 = df["x14_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x14_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta14a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P15 Soporte Técnico
rta15_a = 'answer661992X506X16513'
def answers15(driver, df, rta15a, user_id):
    #definimos las posibles respuestas a la pregunta
    x15_11 = df["x15_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x15_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta15a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P16 Especialista en Seguridad de la Información
rta16_a = 'answer661992X506X16509'
def answers16(driver, df, rta16a, user_id):
    #definimos las posibles respuestas a la pregunta
    x16_11 = df["x16_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x16_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta16a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P17 Implementador Configuration Manager
rta17_a = 'answer661992X506X16510'
def answers17(driver, df, rta17a, user_id):
    #definimos las posibles respuestas a la pregunta
    x17_11 = df["x17_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x17_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta17a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P18 Implementador Software de Gestión
rta18_a = 'answer661992X506X16511SQ001_SQ001'
def answers18(driver, df, rta18a, user_id):
    #definimos las posibles respuestas a la pregunta
    x18_11 = df["x18_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x18_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta18a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P19 QA Automation
rta19_a = 'answer661992X506X16578'
def answers19(driver, df, rta19a, user_id):
    #definimos las posibles respuestas a la pregunta
    x19_11 = df["x19_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x19_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta19a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P20 DevOps
rta20_a = 'answer661992X506X16579'
def answers20(driver, df, rta20a, user_id):
    #definimos las posibles respuestas a la pregunta
    x20_11 = df["x20_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x20_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta20a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

#P21 Experto en Machine Learning
rta21_a = 'answer661992X506X16577'
def answers21(driver, df, rta21a, user_id):
    #definimos las posibles respuestas a la pregunta
    x21_11 = df["x21_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x21_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta21a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

submit_class = 'button[id="ls-button-submit"]'
def submit(driver, element_class):
    #enviamos las respuestas
    enviar = driver.find_element(By.CSS_SELECTOR,element_class) 
    enviar.click()
    return driver

sm = WindowManager()
screens = [Introduccion(name="intro") , MainWindow(name="main"), Perfil1(name="perfil1"), Perfil1b(name="perfil1b"),
            Perfil2a(name="perfil2a"), Perfil2b(name="perfil2b"), Perfil2c(name="perfil2c"),
            Perfil3(name="perfil3"), Perfil4(name="perfil4"), 
            Perfil5(name="perfil5"), Perfil6(name="perfil6"), Perfil7(name="perfil7"), 
            Perfil8(name="perfil8"), Perfil9(name="perfil9"), Perfil10(name="perfil10"), 
            Perfil11(name="perfil11"), Perfil12(name="perfil12"), Perfil13(name="perfil13"), 
            Perfil14(name="perfil14"), Perfil15(name="perfil15"), Perfil16(name="perfil16"), 
            Perfil17(name="perfil17"), Perfil18(name="perfil18"), Perfil19(name="perfil19"),
            Perfil20(name="perfil20"), Perfil21(name="perfil21")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "intro"

class FormularioTECx(App):
    def build(self):
        self.icon = 'TECx.png'
        return sm

if __name__ == "__main__":
    FormularioTECx().run()
