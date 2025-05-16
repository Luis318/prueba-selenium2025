from selenium.webdriver.common.keys import Keys

from pages.Funciones import Funciones  
from pages.Login import Login


class Registro():
    
    def __init__(self, driver):
        self.driver = driver
        self.f = Funciones(self.driver)
        self.login = Login(self.driver)
        
    
    #Registra un usuario con un empleado existente 
    def registrar_usuario(self, empleado="", usuario="", password=""):
        self.login.iniciar_sesion("Admin", "admin123")
        
        #Revisa si el menu esta desplegado
        menu = self.f.validar_elemento_xpath("//i[@class='oxd-icon bi-chevron-right']")
        
        if menu:    
            self.f.click_boton_xpath("//i[@class='oxd-icon bi-chevron-right']", 1)
        else:
            #Clic al boton de admin
            self.f.click_boton_xpath("//span[text()='Admin']", 1)
            
            #clic al boton de agregar
            self.f.click_boton_xpath("//button[@type='button' and contains(@class, 'oxd-button--secondary')]", 1)
            #clic al select de User Role
            self.f.select_elemento_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[1]/div[1]").send_keys(Keys.DOWN + Keys.ENTER)
            
            #Escribir el nombre del empleado
            self.f.text_xpath("//input[@placeholder='Type for hints...']", empleado)
            self.f.select_elemento_xpath("//input[@placeholder='Type for hints...']").send_keys(Keys.DOWN + Keys.ENTER)
            
            #Seleccionar Status
            self.f.select_elemento_xpath("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]").send_keys(Keys.DOWN + Keys.ENTER)
            
            #Escribir el nombre de usuario
            self.f.text_xpath("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input", usuario)
            
            #Escribir el password
            self.f.text_xpath("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input", password)
            
            #Confirmar el password
            self.f.text_xpath("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input", password)
            
            #Clic al boton de guardar
            self.f.click_boton_xpath("//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
            
            ##Verifica el mensaje de exito
            
            if self.f.validar_elemento_xpath("//*[@id='oxd-toaster_1']/div"):
                print("Usuario creado con exito")
            else:
                print("No se pudo crear el usuario")
            
    def crear_empleado(self, primer_nombre="", segundo_nombre="", apellido=""):       
        self.login.iniciar_sesion("Admin", "admin123")
        
        #Revisa si el menu esta desplegado
        menu = self.f.validar_elemento_xpath("//i[@class='oxd-icon bi-chevron-right']")
        
        if menu:    
            self.f.click_boton_xpath("//i[@class='oxd-icon bi-chevron-right']", 1)
        else:
            #Clic al boton de PIM
            self.f.click_boton_xpath("//span[text()='PIM']", 1)
            
            #clic al boton de agregar
            self.f.click_boton_xpath("//button[@type='button' and contains(@class, 'oxd-button--secondary')]", 1)
            
            #Agregar First Name
            self.f.text_xpath("//input[@placeholder='First Name']", primer_nombre)
            
            #Agregar Middle Name
            self.f.text_xpath("//input[@placeholder='Middle Name']",segundo_nombre)
            
            #agregar Last Name
            self.f.text_xpath("//input[@placeholder='Last Name']", apellido)
            
            #clic en Save
            self.f.click_boton_xpath("//button[@type='submit']")
            
            #verificar si el empleado fue creado
            self.f.validar_elemento_xpath("//*[@id='oxd-toaster_1']/div")
        
    #Eliminar un empleado        
    def eliminar_empleado(self, nombre_empleado=""):
        self.login.iniciar_sesion("Admin", "admin123")
        
        #Revisa si el menu esta desplegado
        menu = self.f.validar_elemento_xpath("//i[@class='oxd-icon bi-chevron-right']")
        
        if menu:    
            self.f.click_boton_xpath("//i[@class='oxd-icon bi-chevron-right']", 1)
        else:
            #Clic al boton de admin
            self.f.click_boton_xpath("//span[text()='PIM']", 1)
            
            #clic en eliminar 
            self.f.clickTagName("//div[@class='oxd-table-card']", "Amelia ", "button", 1)
            
            
            
            