import time
import unittest
import os

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones():
    
    def __init__(self, driver):
        self.driver = driver
        self.reporte_dir = "reportes/capturas"
        os.makedirs(self.reporte_dir, exist_ok=True)
        
    
    def abrir_navegador(self, url):
        self.driver.get(url)
        print("Página abierta: "+ str(url))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(3)
        
    """
        ##Validar que el elemento existe
        ## y es visible
    """
    def validar_elemento_xpath(self, xpath, tiempo=5):
        try:
            elemento = WebDriverWait(self.driver, tiempo).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            print("Elemento encontrado: " + str(xpath))
            return elemento.is_displayed()
        
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento")
            return False
        
    """
        ##Escribir texto en un campo
    """
    def text_xpath(self, xpath, texto, tiempo=3):
        
        if(self.validar_elemento_xpath(xpath)):
            
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            
            print("Escribiendo en el campo: {} el texto: {}".format(xpath, texto))
            t = time.sleep(tiempo)
            return True
        
        else:
            print("No se encontró el elemento")
            return False
    
    """
    #Clic a un boton por xpath
    """
    def click_boton_xpath(self, xpath, tiempo=1):
        
        if(self.validar_elemento_xpath(xpath)):    
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            
            t = time.sleep(tiempo)
            return True
        
        else:
            print("No se encontró el elemento")
            return False
            
    """
        #Seleccionar un elemento de un select por xpath
    """
    def seleccionar_select_xpath(self, xpath, texto, tiempo=1):
        
        if (self.validar_elemento_xpath(xpath)):
            valor = Select(self.driver.find_element(By.XPATH, xpath))
            valor.select_by_visible_text(texto)
            return True
        else:
            print("No se encontró el elemento")
            return False
        
    """
    #Selecciona un elemento por su xpath 
    """
    def select_elemento_xpath(self, xpath, tiempo=1):
        
        if (self.validar_elemento_xpath(xpath)):
            valor = self.driver.find_element(By.XPATH, xpath)
            time.sleep(tiempo)
            return valor
        else:
            print("No se encontró el elemento")
            return False
        
    
    def capturas_pantalla(self, nombre="captura"):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = os.path.join(self.reporte_dir, f"{nombre}_{timestamp}.png")
        self.driver.save_screenshot(path)
        print(f"Captura de pantalla guardada en: {path}")
