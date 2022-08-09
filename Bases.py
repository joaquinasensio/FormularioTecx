import pandas as pd

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
def answers(driver, df, rta1, rta2, user_id):     
    #definimos las posibles respuestas a la pregunta
    x1_11 = df["x1_11"][user_id] #busqueda activa
    x1_12 = df["x1_12"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x1_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta1)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x1_12) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta2)
    text_questions2.send_keys(text_answers2)

    return driver

#P1 Scrum Master / Agile Coach
rta1b_a = 'answer661992X506X16497SQ003_SQ001'
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
    x2b_11 = df["x2_11"][user_id] #busqueda activa
    x2b_12 = df["x2_12"][user_id] #busqueda activa
    x2b_13 = df["x2_13"][user_id] #busqueda activa
    x2b_14 = df["x2_14"][user_id] #busqueda activa
    x2b_15 = df["x2_15"][user_id] #busqueda activa
    
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
    x2c_11 = df["x2_11"][user_id] #busqueda activa
    x2c_12 = df["x2_12"][user_id] #busqueda activa
    x2c_13 = df["x2_13"][user_id] #busqueda activa
    x2c_14 = df["x2_14"][user_id] #busqueda activa
    x2c_15 = df["x2_15"][user_id] #busqueda activa
    
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

