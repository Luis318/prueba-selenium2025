from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()     
driver.get("https://google.com")
driver.maximize_window()

driver.implicitly_wait(10)

time.sleep(3)




driver.close()