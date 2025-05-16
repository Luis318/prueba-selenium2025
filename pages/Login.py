
from pages.Funciones import Funciones

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
        
    def cerrar_sesion(self):
        self.f.click_boton_xpath("//span[@class='oxd-userdropdown-tab']")
        self.f.click_boton_xpath("//a[@class='oxd-userdropdown-link' and text()='Logout']")
        
        if self.f.validar_elemento_xpath("//h5"):
            print("Sesión cerrada con éxito")
        else:
            print("No se pudo cerrar la sesión")