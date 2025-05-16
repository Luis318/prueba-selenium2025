import unittest

from selenium import webdriver
from pages.Funciones import Funciones
from pages.Login import Login
from pages.Registro import Registro

class Test1(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.f = Funciones(self.driver)
        self.login = Login(self.driver)
        self.registro = Registro(self.driver)
        
    
    def test_abrir_navegador(self):
        
        self.f.abrir_navegador("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
    #Test inicio de sesion con exito
    def test_inicio_sesion_exito(self):
        self.login.iniciar_sesion("Admin", "admin123")
        
    
    """
    #Test para cerrar sesion con exito
    """
    def test_cerrar_sesion(self):
        self.login.iniciar_sesion("Admin", "admin123")
        #captura de pantalla
        self.f.capturas_pantalla("InicioSesion")
        
        self.login.cerrar_sesion()
        #captura de pantalla
        self.f.capturas_pantalla("CerrarSesion")
        
        
    """"
    Se verifica que el mensaje de error se muestre
        - al intentar iniciar sesion sin enviar las credenciales
        - al enviar credenciales incorrectas
    """
    def test_inicio_sesion_fallido(self):
        #inicaindo sesion con credenciales incorrectas
        self.login.iniciar_sesion("aaa", "aaaa")
        #Validando mensaje de error si no se envian las credenciales
        self.login.existen_mensajes("//p[text()='Invalid credentials']")
        
    
    """
    #Test para crear un usuario con un empleado existente con exito
    """
    def test_crear_usuario(self):
        self.registro.registrar_usuario("James  Butler", "jperez1", "password123")
        
    
    """
    #Test para crear un usuario con un empleado nuevo con exito
    """
    def test_crear_empleado(self):
        self.registro.crear_empleado("Jorge","Montes","Lopez")
        
    def test_eliminar_empleado(self):
        self.registro.eliminar_empleado()

    
    def tearDown(self):
        self.driver.close()
        
if __name__== "__main__":
    unittest.main()

    