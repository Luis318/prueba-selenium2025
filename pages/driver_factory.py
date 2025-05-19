from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_chorme_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    
    options.add_argument("--window-size=1920x1080")
    
    return webdriver.Chrome(options=options)
    