from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Caminho do Chrome no WSL
chrome_path = "/home/local_us/dash/chrome-linux64/chrome"

# Configuração das opções do Chrome
chrome_options = Options()
chrome_options.binary_location = chrome_path
#chrome_options.add_argument("--headless")  # Rodar sem interface gráfica
#chrome_options.add_argument("--no-sandbox")  # Necessário para rodar em containers/WLS
#chrome_options.add_argument("--disable-dev-shm-usage")  # Previne problemas de memória
chrome_options.add_argument("--remote-debugging-port=9222")  # Permite debugging remoto

# Caminho do WebDriver
service = Service("/home/local_us/dash/chromedriver-linux64/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com")
print("Título da página:", driver.title)

time.sleep(20)
driver.quit()
