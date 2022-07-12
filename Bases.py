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
    x1_21 = df["x1_21"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x1_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta1)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x1_21) #send keys funciona con str, pero llegan al formulario como int
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
    text_questions1 = driver.find_element(By.ID,rta2_a)
    text_questions1.send_keys(text_answers1)        
        
    text_answers2 = str(x2_12) # following the order in the form
    text_questions2 = driver.find_element(By.ID,rta2_b)
    text_questions2.send_keys(text_answers2)     
    
    text_answers3 = str(x2_13) # following the order in the form
    text_questions3 = driver.find_element(By.ID,rta2_c)
    text_questions3.send_keys(text_answers3)        
        
    text_answers4 = str(x2_14) # following the order in the form
    text_questions4 = driver.find_element(By.ID,rta2_d)
    text_questions4.send_keys(text_answers4)      

    text_answers5 = str(x2_15) # following the order in the form
    text_questions5 = driver.find_element(By.ID,rta2_e)
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
    x3_21 = df["x3_21"][user_id] #busqueda activa
    
    #ingresamos los valores
    text_answers1 = str(x3_11) #send keys funciona con str, pero llegan al formulario como int
    text_questions1 = driver.find_element(By.ID,rta3a)
    text_questions1.send_keys(text_answers1)        
     
    #ingresamos los valores
    text_answers2 = str(x3_21) #send keys funciona con str, pero llegan al formulario como int
    text_questions2 = driver.find_element(By.ID,rta3b)
    text_questions2.send_keys(text_answers2)     
    
    return driver

submit_class = 'button[id="ls-button-submit"]'

def submit(driver, element_class):
    #enviamos las respuestas
    enviar = driver.find_element(By.CSS_SELECTOR,element_class) 
    enviar.click()
    return driver

