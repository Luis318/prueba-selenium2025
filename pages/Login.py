
from pages.Funciones import Funciones
from selenium.webdriver.common.by import By

class Login():
    
    def __init__(self, driver):
        self.driver = driver
        self.f = Funciones(self.driver)
    
    def iniciar_sesion(self, usuario, password):
        self.f.abrir_navegador("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.f.text_xpath("//input[@name='username']", usuario)
        self.f.text_xpath("//input[@name='password']", password)
        self.f.click_boton_xpath("//button[@type='submit']")
        
        print("Usuario ingresado: "+ str(usuario))
        
        if self.f.validar_elemento_xpath("//span[@class='oxd-userdropdown-tab']"):
            print("Inicio de sesión exitoso")
            return True
        else:
            print("Error al iniciar sesión")
            return False    
        
        
    def cerrar_sesion(self):
        self.f.click_boton_xpath("//span[@class='oxd-userdropdown-tab']")
        self.f.click_boton_xpath("//a[@class='oxd-userdropdown-link' and text()='Logout']")
        
        if self.f.validar_elemento_xpath("//h5"):
            print("Sesión cerrada con éxito")
            return True
        else:
            print("No se pudo cerrar la sesión")
            return False
    
    
    """
    Verifica si existe un mensaje de error, usando xpath
    - xpath: xpath del mensaje de error
    """
    def existen_mensajes(self, xpath):
        
        if self.f.validar_elemento_xpath(xpath):
            print("Existe un mensaje de error")
            return True
        
        else: 
            print("No se encontró el mensaje de error")
            return False
        
    def validar_texto_alertas(self, xpath, texto_esperado):
        
        if self.f.validar_elemento_xpath(xpath):
            mensaje = self.driver.find_element(By.XPATH, xpath)
            mensaje_texto = mensaje.text
            
            if mensaje_texto == texto_esperado:
                print("Los mesajes de alerta concuerdan")
                print("Mensaje encontrado: " + mensaje_texto)
                return True
            
            else:
                print("Los mensajes de alerta no concuerdan")
                print("Mensaje encontrado: " + mensaje_texto)
                return False
        else:
            print("No se encontró el mensaje de error")
            return False
                