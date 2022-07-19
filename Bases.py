import pandas as pd

#para el web scraping
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from parsel import Selector
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# url = "https://economictrends.limequery.com/214733?token=1234&lang=es"
# driver = webdriver.Chrome(ChromeDriverManager().install())

perfil1_clase = 'button[data-target="#question16379"]'
rta1 = 'answer214733X505X16379SQ001_SQ001'
rta2 = 'answer214733X505X16379SQ002_SQ001'

def answers(driver, df, perfil1_class, rta1, rta2, user_id):
    
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil1_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
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

perfil2_clase = 'button[data-target="#question16389"]'
rta2_a = 'answer214733X505X16389SQ001_SQ001'
rta2_b = 'answer214733X505X16389SQ002_SQ001'
rta2_c = 'answer214733X505X16389SQ003_SQ001'
rta2_d = 'answer214733X505X16389SQ004_SQ001'
rta2_e = 'answer214733X505X16389SQ005_SQ001'

def answers2(driver, df, perfil2_class, rta2a, rta2b, rta2c, rta2d, rta2e, user_id):
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil2_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)

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

perfil3_clase = 'button[data-target="#question16387"]'
rta3_a = 'answer214733X505X16387SQ001_SQ001'
rta3_b = 'answer214733X505X16387SQ002_SQ001'

def answers3(driver, df, perfil3_class, rta3a, rta3b, user_id):
    
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil3_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
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

perfil4_clase = 'button[data-target="#question16388"]'
rta4_a = 'answer214733X505X16388SQ001_SQ001'
rta4_b = 'answer214733X505X16388SQ002_SQ001'
rta4_c = 'answer214733X505X16388SQ003_SQ001'

def answers4(driver, df, perfil4_class, rta4a, rta4b, rta4c, user_id):
    
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil4_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
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

perfil5_clase = 'button[data-target="#question16383"]'
rta5_a = 'answer214733X505X16383SQ001_SQ001'
rta5_b = 'answer214733X505X16383SQ002_SQ001'
rta5_c = 'answer214733X505X16383SQ003_SQ001'

def answers5(driver, df, perfil5_class, rta5a, rta5b, rta5c, user_id):
    
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil5_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
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

perfil6_clase = 'button[data-target="#question16390"]'
rta6_a = 'answer214733X505X16390SQ001_SQ001'
rta6_b = 'answer214733X505X16390SQ002_SQ001'
rta6_c = 'answer214733X505X16390SQ003_SQ001'

def answers6(driver, df, perfil6_class, rta6a, rta6b, rta6c, user_id):
    
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil6_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
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

perfil7_clase = 'button[data-target="#question16386"]'
rta7_a = 'answer214733X505X16386SQ001_SQ001'
rta7_b = 'answer214733X505X16386SQ002_SQ001'
rta7_c = 'answer214733X505X16386SQ003_SQ001'
rta7_d = 'answer214733X505X16386SQ004_SQ001'

def answers7(driver, df, perfil7_class, rta7a, rta7b, rta7c, rta7d, user_id):
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil7_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)

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

perfil8_clase = 'button[data-target="#question16396"]'
rta8_a = 'answer214733X505X16396SQ001_SQ001'
rta8_b = 'answer214733X505X16396SQ002_SQ001'
rta8_c = 'answer214733X505X16396SQ003_SQ001'

def answers8(driver, df, perfil8_class, rta8a, rta8b, rta8c, user_id):
    
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil8_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
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

perfil9_clase = 'button[data-target="#question16382"]'
rta9_a = 'answer214733X505X16382SQ001_SQ001'
rta9_b = 'answer214733X505X16382SQ002_SQ001'
rta9_c = 'answer214733X505X16382SQ003_SQ001'

def answers9(driver, df, perfil9_class, rta9a, rta9b, rta9c, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil9_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
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

perfil10_clase = 'button[data-target="#question16394"]'
rta10_a = 'answer214733X505X16394SQ001_SQ001'
rta10_b = 'answer214733X505X16394SQ002_SQ001'
rta10_c = 'answer214733X505X16394SQ003_SQ001'
rta10_d = 'answer214733X505X16394SQ004_SQ001'
rta10_e = 'answer214733X505X16394SQ005_SQ001'
rta10_f = 'answer214733X505X16394SQ006_SQ001'

def answers10(driver, df, perfil10_class, rta10a, rta10b, rta10c, rta10d, rta10e, rta10f, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil10_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
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

perfil11_clase = 'button[data-target="#question16380"]'
rta11_a = 'answer214733X505X16380'

def answers11(driver, df, perfil11_class, rta11a, user_id):
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil11_class) 
    driver.implicitly_wait(10)
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
    #definimos las posibles respuestas a la pregunta
    x11_11 = df["x11_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x11_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta11a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

perfil12_clase = 'button[data-target="#question16384"]'
rta12_a = 'answer214733X505X16384'

def answers12(driver, df, perfil12_class, rta12a, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil12_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
    #definimos las posibles respuestas a la pregunta
    x12_11 = df["x12_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x12_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta12a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

perfil13_clase = 'button[data-target="#question16381"]'
rta13_a = 'answer214733X505X16381'

def answers13(driver, df, perfil13_class, rta13a, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil13_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
    #definimos las posibles respuestas a la pregunta
    x13_11 = df["x13_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x13_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta13a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

perfil14_clase = 'button[data-target="#question16385"]'
rta14_a = 'answer214733X505X16385'

def answers14(driver, df, perfil14_class, rta14a, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil14_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
    #definimos las posibles respuestas a la pregunta
    x14_11 = df["x14_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x14_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta14a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

perfil15_clase = 'button[data-target="#question16395"]'
rta15_a = 'answer214733X505X16395'

def answers15(driver, df, perfil15_class, rta15a, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil15_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
    #definimos las posibles respuestas a la pregunta
    x15_11 = df["x15_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x15_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta15a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

perfil16_clase = 'button[data-target="#question16391"]'
rta16_a = 'answer214733X505X16391'

def answers16(driver, df, perfil16_class, rta16a, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil16_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
    #definimos las posibles respuestas a la pregunta
    x16_11 = df["x16_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x16_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta16a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

perfil17_clase = 'button[data-target="#question16392"]'
rta17_a = 'answer214733X505X16392'

def answers17(driver, df, perfil17_class, rta17a, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil17_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
    #definimos las posibles respuestas a la pregunta
    x17_11 = df["x17_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x17_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta17a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

perfil18_clase = 'button[data-target="#question16393"]'
rta18_a = 'answer214733X505X16393SQ001_SQ001'

def answers18(driver, df, perfil18_class, rta18a, user_id):
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil18_class) 
    driver.execute_script("arguments[0].click();",titulo_click)
    driver.implicitly_wait(3)
    
    #definimos las posibles respuestas a la pregunta
    x18_11 = df["x18_11"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x18_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta18a)
    text_questions1.send_keys(text_answers1)        
         
    return driver

submit_class = 'button[id="ls-button-submit"]'

def submit(driver, element_class):
    #enviamos las respuestas
    enviar = driver.find_element(By.CSS_SELECTOR,element_class) 
    enviar.click()
    return driver

