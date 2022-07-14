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

def answers(driver, df, perfil_class, rta1, rta2, user_id):
    
    #expandimos la pregunta
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil_class) 
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

def answers2(driver, df, perfil_class, rta2a, rta2b, rta2c, rta2d, rta2e, user_id):
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil_class) 
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
    driver.implicitly_wait(10)
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
    driver.implicitly_wait(10)
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
    driver.implicitly_wait(10)
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
    driver.implicitly_wait(10)
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

def answers7(driver, df, perfil_class, rta7a, rta7b, rta7c, rta7d, user_id):
    titulo_click = driver.find_element(By.CSS_SELECTOR,perfil_class) 
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
    driver.implicitly_wait(10)
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

submit_class = 'button[id="ls-button-submit"]'

def submit(driver, element_class):
    #enviamos las respuestas
    enviar = driver.find_element(By.CSS_SELECTOR,element_class) 
    enviar.click()
    return driver

